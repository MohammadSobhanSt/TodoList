<script setup>
import { ref, watch } from "vue"
import Draggable from "vuedraggable"
import { SquarePen, Shredder, Check, X } from "@lucide/vue"

let id = 0

const defaultTasks = [
  { id: 0, title: "Deploy Project", description: "", completed: false, showDescription: false },
]

const tasks = ref(JSON.parse(localStorage.getItem("tasks")) || defaultTasks)

watch(tasks,
  (newTasks) => {
    localStorage.setItem("tasks", JSON.stringify(newTasks))},
    { deep: true })

// We could write the code above like:
// function saveTasks(newTasks) {
//   localStorage.setItem("tasks", JSON.stringify(newTasks))},
//   { deep: true }
// 
// watch(tasks, saveTasks)


function showDes(task) {
  task.showDescription = !task.showDescription
}

const addTaskInput = ref('')
const addDescriptionInput = ref('')

function addTask() {
  if (addTaskInput.value){
    tasks.value.push({ id: id++, title: addTaskInput.value, description: addDescriptionInput.value, completed: false, showDescription: false })
    addTaskInput.value = ''
    addDescriptionInput.value = ''
  };
}

var showAddTask = ref(true)

const editingTaskId = ref(null)
const vFocus = {
  mounted: (el) => el.focus()
}
</script>

<template>
    <h5 class="text-center">ToDo List</h5><br>
    <div class="text-center">
        <span id="showAddTaskBtn" @click.prevent="showAddTask = !showAddTask">
            {{ showAddTask ? 'Hide form' : 'Show form' }}
        </span>
    </div>
    <div v-show="showAddTask">
        <div class="d-flex justify-content-center mx-2">
            <div class="card" id="addTaskCard">
                <div class="card-body">
                    <div class="card-title">
                        <h5 class="text-white">New Task</h5>
                    </div>
                    <span class="text-danger">*</span>
                    <input type="text" class="form-control" placeholder="add a task" id="addTaskInput" @keyup.enter="addTask()" v-model="addTaskInput"/>
                    <br>
                    <textarea class="form-control" placeholder="add a description" id="addDescriptionInput" @keyup.enter="addTask()" v-model="addDescriptionInput"/>
                    <br>
                    <div class="d-flex justify-content-center">
                        <button type="submit" class="btn btn-primary mx-2" id="addTaskButton" @click="addTask()">add</button>    
                    </div>
                </div>
            </div>
        </div>
    </div>
    <hr>
    <Draggable v-model="tasks" item-key="id" animation="500">
        <template #item="{ element }">
            <div class="d-flex justify-content-center">
                <div class="card">
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="d-flex align-items-center">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" v-model="element.completed"/>
                                </div>
                                <label v-if="editingTaskId !== element.id">
                                    <s v-if="element.completed">{{ element.title }}</s>
                                    <span v-else>{{ element.title }}</span>
                                </label>
                                <input type="text" class="editInput" id="editInput" v-else v-focus v-model="element.title" @keyup.enter="editingTaskId = null, element.title = editInput.value" @blur="editingTaskId = null"/>
                            </div>
                            <div class="d-flex gap-2 align-items-center" v-if="editingTaskId !== element.id">
                                <SquarePen size="16" id="squarePen" @click="editingTaskId = element.id"/>
                                <Shredder size="16" class="text-danger" id="shredder"/>
                            </div>
                            <div class="d-flex gap-2 align-items-center" v-else>
                                <Check size="16" id="squarePen" @click="element.title = editInput.value"/>
                                <X size="16" id="shredder" @click="editingTaskId = null"/>
                            </div>
                        </div>
                        <div v-show="element.showDescription">
                            <hr style="width: 7rem;">{{ element.description }}
                        </div>
                    </div>
                    <small v-if="element.description" class="d-flex justify-content-end">
                        <span id="showDescription" @click="showDes(element)">
                            ...
                        </span>
                    </small>
                </div>
            </div>
        </template>
    </Draggable>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap');

.card {
  font-family: "Vazirmatn", sans-serif;
  padding: 10px;
  margin: 8px 0;
  width: 20rem;
  min-height: 4rem;
  border: 1px solid #7a7d7b;
  color: lightgoldenrodyellow;
}

.form-check-input:checked {
  background-color: #133b38;
  border-color: #133b38;
}

#addTaskInput {
 width: 32rem;
}

#addDescriptionInput {
 width: 32rem;
}

#addTaskButton {
    width: 5rem;
}

#showDescription {
    color: #7a7d7b;
    cursor: pointer;
}

#addTaskCard {
    width: 35rem;
    height: 18rem;
}

#showAddTaskBtn {
    color: lightgray;
    cursor: pointer;
    user-select: none;
}

#squarePen, #shredder {
    cursor: pointer;
}

.editInput {
  border: none;
  outline: none;
  background: transparent;
  font: inherit;
  color: inherit;
  width: 100%;
  padding: 0;
}

.editInput:focus {
  outline: none;
}
</style>