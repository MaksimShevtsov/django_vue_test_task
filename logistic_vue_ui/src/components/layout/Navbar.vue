<template>
    <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Logistic App</strong>
            </router-link>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
                <div class="navbar-start">
                    <div class="buttons">
                        <router-link to="/orders" class="button is-light"><strong>Orders</strong></router-link>
                        <router-link to="/customers" class="button is-light"><strong>Customers</strong></router-link>
                        <router-link to="/shippingmethod" class="button is-light"><strong>Shipping method</strong></router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {
        name: 'Navbar'
    }
</script>