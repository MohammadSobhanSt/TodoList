import { ref } from "vue";

const authenticated = ref(!!localStorage.getItem("accessToken"));

export function isAuthenticated() {
    return authenticated;
}