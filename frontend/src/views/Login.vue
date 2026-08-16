<script setup>
import axios from "axios";
import { ref } from "vue";
import Message from "../components/Message.vue";

const username = ref("");
const password = ref("");

const messages = ref([]);
const messageType = ref("");

async function login() {
    messages.value = [];

    try {
        const response = await axios.post("http://localhost:8000/api/token/", {
            username: username.value,
            password: password.value,
        });

        messages.value = ["Login successful!"];
        messageType.value = "success";

        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("refreshToken", response.data.refresh);

        window.location.reload();
    } catch (error) {
        messageType.value = "danger";

        if (error.response && error.response.data) {
            messages.value = Object.values(error.response.data).flat();
        } else {
            messages.value = ["Something went wrong."];
        }
    }
}
</script>

<template>
    <Message v-if="messages.length" :messages="messages" :tag="messageType" />

    <div class="d-flex justify-content-center">
        <div class="card shadow-lg p-3">
            <div class="card-body">
                <form @submit.prevent="login">
                    <h1 class="h3 mb-3 fw-normal">Login Page</h1>

                    <hr />
                    <br />

                    <div>
                        <label for="floatingInput"> Username </label>

                        <input
                            type="text"
                            class="form-control"
                            id="floatingInput"
                            placeholder="Enter your username"
                            autofocus
                            v-model="username"
                        />
                    </div>

                    <br />

                    <div>
                        <label for="floatingPassword"> Password </label>

                        <input
                            type="password"
                            class="form-control"
                            id="floatingPassword"
                            placeholder="Enter your password"
                            v-model="password"
                        />
                    </div>

                    <br />

                    <button
                        class="btn btn-outline-light"
                        type="submit"
                        id="loginButton"
                    >
                        Login
                    </button>

                    <hr />

                    <p>
                        Don't you have an account?

                        <router-link :to="{ name: 'signup' }">
                            <strong class="text-white"> SignUp </strong>
                        </router-link>
                    </p>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card {
    width: 25rem;
    border: 1px solid rgba(255, 255, 255, 0.07);
}

#loginButton {
    width: 100px;
    margin: 0 auto;
    display: block;
}
</style>
