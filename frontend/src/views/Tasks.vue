<script setup>
import { ref } from "vue"
import Draggable from "vuedraggable"

let id = 0

const tasks = ref([
  { id: 1, title: "کامل کردن فرانت", description: "", completed: false, showDescription: false},
  { id: 2, title: "Build Todo App", description: "", completed: false, showDescription: false},
  { id: 3, title: "Deploy Project", description: "", completed: false, showDescription: false},
])

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
</script>

<template>
    <h5 class="text-center">ToDo List</h5><br>
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
    <hr>
    <Draggable v-model="tasks" item-key="id" animation="500">
        <template #item="{ element }">
            <div class="d-flex justify-content-center">
                <div class="card">
                    <div class="card-body">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" :id="'check-' + element.id" v-model="element.completed"/>
                            <label class="form-check-label" :for="'check-' + element.id" @click.prevent>
                                <s v-if="element.completed">{{ element.title }}</s>
                                <span v-else>{{ element.title }}</span>
                                <span v-show="element.showDescription"><hr>{{ element.description }}</span>
                            </label>
                        </div>
                    </div>
                    <span v-if="element.description" class="d-flex justify-content-end" id="showDescription" @click="showDes(element)">...</span>
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
</style>