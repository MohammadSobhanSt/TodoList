<script setup>
import { ref } from "vue";
import axios from "axios";
import Message from "../components/Message.vue";

const username = ref("");
const password = ref("");
const confirmPassword = ref("");
const messages = ref([]);
const messageType = ref("");

async function signup() {
    try {
        const signupResponse = await axios.post(
            "http://127.0.0.1:8000/accounts/signup/",
            {
                username: username.value,
                password1: password.value,
                password2: confirmPassword.value,
            },
        );

        messages.value = [
            "Your account was created successfully. You can login now.",
        ];

        messageType.value = "success";
    } catch (error) {
        messageType.value = "danger";
        messages.value = [];

        if (error.response) {
            const errors = error.response.data;

            for (const errorMessages of Object.values(errors)) {
                messages.value.push(...errorMessages);
            }
        } else {
            messages.value = ["Signup failed."];
        }
    }
}
</script>

<template>
    <Message v-if="messages.length" :messages="messages" :tag="messageType" />
    <div class="d-flex justify-content-center">
        <div class="card shadow-lg p-3">
            <div class="card-body">
                <form @submit.prevent="signup">
                    <h1 class="h3 mb-3 fw-normal">SignUp Page</h1>
                    <hr />
                    <br />
                    <div>
                        <label for="floatingInput">Username</label>
                        <input
                            type="text"
                            class="form-control"
                            id="usernameInput"
                            placeholder="Enter your username"
                            autofocus="autofocus"
                            v-model="username"
                        />
                    </div>
                    <br />
                    <div>
                        <label for="floatingInput">Password</label>
                        <input
                            type="password"
                            class="form-control"
                            id="passwordInput"
                            placeholder="Enter your password"
                            autofocus="autofocus"
                            v-model="password"
                        />
                    </div>
                    <br />
                    <div>
                        <label for="floatingPassword">Confirm Password</label>
                        <input
                            type="password"
                            class="form-control"
                            id="confirmPasswordInput"
                            placeholder="Confirm your password"
                            v-model="confirmPassword"
                        />
                    </div>
                    <br />
                    <button
                        class="btn btn-outline-warning"
                        id="loginButton"
                        type="submit"
                    >
                        SignUp
                    </button>
                    <hr />
                    <p>
                        Already have an account?
                        <router-link :to="{ name: 'login' }"
                            ><strong class="text-white"
                                >Login</strong
                            ></router-link
                        >
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
    box-shadow: 1px 3px 10px #b0b0b0;
}
#loginButton {
    width: 100px;
    margin: 0 auto;
    display: block;
}
</style>
