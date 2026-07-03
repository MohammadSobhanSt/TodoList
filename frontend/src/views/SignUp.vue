<template>
    <div class="d-flex justify-content-center">
        <div class="card shadow-lg">
            <div class="card-body">
                <form>
                    <h1 class="h3 mb-3 fw-normal">SignUp Page</h1>
                    <hr><br>
                    <div> 
                        <label for="floatingInput">Email address</label>
                        <input type="email" class="form-control" id="floatingInput" placeholder="email@example.com" autofocus="autofocus">
                    </div>
                    <br>
                    <div> 
                        <label for="floatingInput">Username</label>
                        <input type="email" class="form-control" id="floatingInput" placeholder="Enter your username" autofocus="autofocus">
                    </div>
                    <br>
                    <div>
                        <label for="floatingPassword">Password</label>
                        <input type="password" class="form-control" id="floatingPassword" placeholder="Enter your Password">
                    </div>
                    <br>
                    <button class="btn btn-outline-warning" type="submit" id="loginButton">SignUp</button>
                    <hr>
                    <p>Already have an account? <router-link :to="{name: 'login'}"><strong class="text-white">Login</strong></router-link></p>

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