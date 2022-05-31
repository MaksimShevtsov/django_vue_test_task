<template>
  <div class="container">
    <div class="container is-multiline">
      <div class="column is-12">
        <h1 class="title is-1 is-spaced has-text-centered">
            Vue JS Front End
        </h1>
        <h2 class="subtitle has-text-centered">
            REST API functionality to maintain a list of shipments
        </h2>
        <router-view></router-view>
      </div>
    </div>
    <div class="column is-12 has-text-centered py-6">
      <router-link to="/orders" class="button is-primary"><strong>Demo</strong></router-link>
    </div>
  </div>  
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
