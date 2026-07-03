<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link :to="{name: 'home'}" class="navbar-brand">Home</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarScroll">
                <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
                    <li class="nav-item">
                        <router-link :to="{name: 'tasks'}" class="nav-link">Tasks</router-link>
                    </li>
                </ul>
                <router-link :to="{ name: 'login' }" class="btn btn-outline-light mx-2">Login</router-link>
                <router-link :to="{ name: 'signup' }" class="btn btn-outline-warning">Signup</router-link>
            </div>
        </div>
    </nav>
    <br>
</template>
