import { createRouter, createWebHistory } from "vue-router";
import SignUp from "../views/SignUp.vue";
import Login from "../views/Login.vue";
import Tasks from "../views/Tasks.vue";
import Home from "../views/Home.vue";
import { isAuthenticated } from "@/composables/IsAuthenticated";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignUp,
    beforeEnter: () => {
      if (isAuthenticated().value) {
        return { name: "tasks" };
      }
    },
  },
  {
    path: "/login",
    name: "login",
    component: Login,
    beforeEnter: () => {
      if (isAuthenticated().value) {
        return { name: "tasks" };
      }
    },
  },
  {
    path: "/tasks",
    name: "tasks",
    component: Tasks,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
