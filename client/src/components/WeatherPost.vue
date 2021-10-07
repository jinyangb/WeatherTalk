<template>
  <section class="post">
    <div>
      <h4>{{ post.temperature }}&#176;</h4>
      <p>{{ post.summary  }}</p>
      <img :src="post.icon_source" />
    </div>
    <div>
      <h4>{{ post.name }}</h4>
      <h4>{{ post.location }}</h4>
      <p>{{ post.content }}</p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'WeatherPost',
  props: {
    post: {}
  }
}
</script>

<style scoped>
  .post {
    display: flex
  }
</style>