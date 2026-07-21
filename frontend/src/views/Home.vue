<template>
    <div class="d-flex flex-column align-items-center gap-3">
        <div>
            <p class="alert alert-info loginMessage">
                Welcome to our website :). Please
                <router-link :to="{ name: 'login' }" class="text-danger">
                    login
                </router-link>
                for being synced with your other devices.
            </p>
        </div>
        <div>
            <p class="alert alert-warning loginMessage">
                You can go to
                <router-link :to="{ name: 'tasks' }">
                    this page
                </router-link>
                to add new tasks without logging in :).
            </p>
        </div>
    </div>
</template>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap');
    
    .loginMessage {
        width: 40rem;
    }
    
    .alert-info {
        font-family: "Caveat", cursive;
        font-optical-sizing: auto;
        font-weight: 700;
        font-size: 1.4rem;
        border-color: white;
        color: lightyellow;
    }
    .alert-warning {
        font-family: "Caveat", cursive;
        font-optical-sizing: auto;
        font-weight: 700;
        font-size: 1.4rem;
    }
</style>