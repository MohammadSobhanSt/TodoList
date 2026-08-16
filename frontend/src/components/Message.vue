<script setup>
defineProps({
    tag: {
        type: String,
        required: true,
    },
    messages: {
        type: Array,
        required: true,
    },
});
</script>

<template>
    <div v-for="(msg, index) in messages" :key="index">
        <div :class="['alert', tag]">
            <div class="message-body">
                <p>{{ msg }}</p>
            </div>
        </div>
    </div>
    <hr />
</template>

<style scoped>
.success {
    background-color: rgba(0, 156, 74, 0.04);
    color: lightyellow;
    border: 1px solid aquamarine;
    height: 3.5rem;
    margin: 6px;
    display: inline-block;
    position: relative;
}

.success::before {
    content: "";
    position: absolute;
    left: 0px;
    top: 50%;
    transform: translateY(-50%);
    width: 5px;
    height: 3.03rem;
    background-color: aquamarine;
    border-radius: 1.5px;
}

.danger {
    background-color: rgba(125, 24, 24, 0.2);
    color: lightyellow;
    border: 1px solid indianred;
    height: 3.5rem;
    margin: 6px;
    display: inline-block;
    position: relative;
}

.danger::before {
    content: "";
    position: absolute;
    left: 0px;
    top: 50%;
    transform: translateY(-50%);
    width: 5px;
    height: 3.03rem;
    background-color: indianred;
    border-radius: 1.5px;
}

.warning {
    background-color: rgba(255, 221, 0, 0.05);
    color: white;
    border: 1px solid #ffa600;
    height: 3.5rem;
    margin: 6px;
    display: inline-block;
    position: relative;
}

.warning::before {
    content: "";
    position: absolute;
    left: 0px;
    top: 50%;
    transform: translateY(-50%);
    width: 5px;
    height: 3.03rem;
    background-color: #ffcb21;
    border-radius: 1.5px;
}

.info {
    background-color: rgba(33, 160, 207, 0.05);
    color: lightyellow;
    border: 1px solid powderblue;
    height: 3.5rem;
    margin: 6px;
    display: inline-block;
    position: relative;
}

.info::before {
    content: "";
    position: absolute;
    left: 0px;
    top: 50%;
    transform: translateY(-50%);
    width: 5px;
    height: 3.03rem;
    background-color: powderblue;
    border-radius: 1.5px;
}

#xButton:hover {
    cursor: pointer;
    color: lightgray;
}
</style>
