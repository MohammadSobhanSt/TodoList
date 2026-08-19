<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import Message from "../components/Message.vue";
import { isAuthenticated } from "@/composables/IsAuthenticated.js";
import Draggable from "vuedraggable";
import { GripVertical, SquarePen, Shredder, Check, X } from "@lucide/vue";

const showTask = ref(true);

const notLoggedIn = ref([
    "You are not logged in, to see your tasks please login first :).",
]);
const tasks = ref([]);
const messages = ref([]);
const messageType = ref("");
const noTaskMsg = ref(["You have no tasks yet..."]);

const authenticated = isAuthenticated();

const title = ref("");
const description = ref("");
const startTime = ref(new Date().toISOString().split("T")[0]);
const deadline = ref("");

const token = localStorage.getItem("accessToken");

localStorage.setItem("tasks", JSON.stringify(tasks));

async function getTasks() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/tasks/list/", {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });

        tasks.value = response.data;
    } catch (e) {
        messages.value = [];
        const error = e.response?.data;

        if (error?.code === "token_not_valid") {
            messages.value.push("You are not logged in.");
        } else if (error) {
            messages.value.push(error);
        }
        messageType.value = "danger";
    }
}

async function addTask() {
    try {
        const response = await axios.post(
            "http://127.0.0.1:8000/tasks/new-task/",
            {
                title: title.value,
                description: description.value,
                start_time: startTime.value,
                deadline: deadline.value || null,
            },
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            },
        );
        await getTasks();

        title.value = "";
        description.value = "";
        deadline.value = "";
    } catch (e) {
        messages.value = [];
        const error = e.response?.data;

        if (error?.code === "token_not_valid") {
            messages.value.push("You are not logged in.");
        } else if (error) {
            messages.value.push(error);
        }
        messageType.value = "danger";
    }
}

async function deleteTask(task) {
    try {
        const response = await axios.delete(
            `http://127.0.0.1:8000/tasks/delete/${task}/`,
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            },
        );
        await getTasks();
    } catch (e) {
        messages.value = [];
        const error = e.response?.data;

        if (error?.code === "token_not_valid") {
            messages.value.push("You are not logged in.");
        } else if (error) {
            messages.value.push(error);
        }
        messageType.value = "danger";
    }
}

async function toggleTaskCompleted(task) {
    try {
        const updatedTask = !task.completed;
        await axios.patch(
            `http://127.0.0.1:8000/tasks/edit/${task.pk}/`,
            {
                completed: updatedTask,
            },
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            },
        );

        task.completed = updatedTask;
    } catch (e) {
        messages.value = [];
        const error = e.response?.data;

        if (error?.code === "token_not_valid") {
            messages.value.push("You are not logged in.");
        } else if (error) {
            messages.value.push(error);
        }
        messageType.value = "danger";
    }
}

async function editTask(task) {
    try {
        const response = await axios.put(
            `http://127.0.0.1:8000/tasks/edit/${task.pk}/`,
            {
                title: task.title,
                description: task.description,
                start_time: task.start_time,
                deadline: task.deadline || null,
            },
            {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            },
      );
      editingTask.value = null;
    } catch (e) {
        messages.value = [];
        const error = e.response?.data;

        if (error?.code === "token_not_valid") {
            messages.value.push("You are not logged in.");
        } else if (error) {
            messages.value.push(error);
        }
        messageType.value = "danger";
    }
}

const showDetail = ref(null);
const editingTask = ref(null);

onMounted(() => {
    if (authenticated.value && !!localStorage.getItem("tasks")) {
        getTasks();
    }
});
</script>

<template>
    <Message v-if="!authenticated" :messages="notLoggedIn" tag="warning" />
    <div v-show="authenticated">
        <Message
            v-if="messages.length"
            :messages="messages"
            :tag="messageType"
        />

        <div>
            <Message
                v-if="tasks.length === 0"
                tag="info"
                :messages="noTaskMsg"
            />

            <div class="d-flex flex-column align-items-center">
                <span @click="showTask = !showTask" id="taskBox">
                    {{ showTask ? "Hide task box" : "Show task box" }}
                </span>
                <br />
                <div>
                    <form v-show="showTask" @submit.prevent="addTask">
                        <div class="card" style="width: 25rem">
                            <div class="card-header"><h4>New task</h4></div>
                            <div class="card-body">
                                <label for="taskInput"
                                    ><b
                                        >Title
                                        <small class="text-danger">*</small></b
                                    ></label
                                >
                                <input
                                    class="form-control"
                                    type="text"
                                    id="taskInput"
                                    placeholder="Enter a title"
                                    v-model="title"
                                />
                                <br />
                                <label for="descriptionInput"
                                    ><b>Description</b></label
                                >
                                <textarea
                                    class="form-control"
                                    type="textarea"
                                    id="descriptionInput"
                                    placeholder="Enter a description"
                                    v-model="description"
                                />
                                <br />
                                <label for="dateInput"
                                    ><b
                                        >Start time
                                        <small class="text-danger">*</small></b
                                    ></label
                                >
                                <input
                                    class="form-control"
                                    type="date"
                                    id="dateInput"
                                    v-model="startTime"
                                />
                                <br />
                                <label for="dateInput"><b>Deadline</b></label>
                                <input
                                    class="form-control"
                                    type="date"
                                    id="dateInput"
                                    v-model="deadline"
                                />
                                <br />
                                <div class="d-flex justify-content-center">
                                    <button
                                        type="submit"
                                        class="btn btn-primary"
                                        style="width: 10rem"
                                    >
                                        New task
                                    </button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <br />

            <Draggable
                v-model="tasks"
                item-key="pk"
                animation="400"
                handle="#gripVertical"
                :disabled="editingTask !== null"
            >
                <template #item="{ element }">
                    <div class="d-flex justify-content-center">
                        <div class="custom-card">
                            <div
                                class="custom-card-body d-flex justify-content-between align-items-center"
                            >
                                <div v-if="editingTask !== element.pk">
                                    <div class="form-check">
                                        <input
                                            class="form-check-input"
                                            type="checkbox"
                                            :checked="element.completed"
                                            @change="toggleTaskCompleted(element)"
                                        />
                                        <span v-if="!element.completed">{{ element.title }}</span>
                                        <s v-else>{{ element.title }}</s>
                                    </div>
                                </div>
                                <input v-else class="form-control mx-2" type="text" v-model="element.title" autofocus="autofocus"/>

                                <div v-if="editingTask !== element.pk" class="d-flex align-items-center gap-1">
                                    <SquarePen size="18" class="icon-btn" @click="editingTask = element.pk; showDetail = element.pk"/>
                                    <Shredder
                                        size="18"
                                        class="icon-btn text-danger"
                                        @click="deleteTask(element.pk)"
                                    />
                                    <GripVertical id="gripVertical" size="18" />
                                </div>
                                <div v-else class="d-flex align-items-center gap-1">
                                    <Check class="text-success icon-btn" size="16" @click="editTask(element)"/>
                                    <X class="text-danger icon-btn" size="17" @click="editingTask = null; showDetail = null"/>
                                </div>
                            </div>
                            <div v-if="showDetail === element.pk && editingTask !== element.pk">
                                <hr />
                                <p v-if="element.description">
                                    <strong>Description: </strong
                                    >{{ element.description }}
                                </p>
                                <p>
                                    <strong>Start time: </strong
                                    >{{ element.start_time }}
                                </p>
                                <p v-if="element.deadline">
                                    <strong>Deadline: </strong
                                    >{{ element.deadline }}
                                </p>
                            </div>
                            <div v-if="showDetail === element.pk && editingTask === element.pk">
                                <hr />
                                <p>
                                    <strong>Description: </strong>
                                    <textarea class="form-control" v-model="element.description"/>
                                </p>
                                <p>
                                    <strong>Start time: </strong>
                                    <input type="date" class="form-control" v-model="element.start_time"/>
                                </p>
                                <p>
                                    <strong>Deadline: </strong>
                                    <input type="date" class="form-control" v-model="element.deadline"/>
                                </p>
                            </div>
                            <small
                                id="showMore"
                                @click="
                                    showDetail =
                                        showDetail === element.pk
                                            ? null
                                            : element.pk
                                "
                                >...</small
                            >
                        </div>
                    </div>
                </template>
            </Draggable>
        </div>
    </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap");

#taskBox {
    cursor: pointer;
    color: lightyellow;
}

.card {
    font-family: "Vazirmatn", sans-serif;
}

.form-check-input:checked {
  background-color: #133b38;
  border-color: #133b38;
}

.custom-card {
    font-family: "Vazirmatn", sans-serif;
    padding: 10px;
    margin: 8px 0;
    width: 30rem;
    min-height: 4rem;
    border: 1px solid #7a7d7b;
    border-radius: 10px;
    color: lightgoldenrodyellow;
}

.custom-card-body label,
.custom-card-body span {
    word-wrap: break-word;
    overflow-wrap: break-word;
    max-width: 20rem;
    display: inline-block;
}

#gripVertical {
    cursor: grab;
    color: gray;
}

#gripVertical:active {
    cursor: grabbing;
}

.dragging #gripVertical,
.dragging {
    cursor: grabbing !important;
}

#showMore {
    cursor: pointer;
}

.icon-btn {
    cursor: pointer;
}
</style>
