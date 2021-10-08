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
    display: flex;
    border: 3px solid black;
    border-radius: 15px;
    justify-content:space-evenly;
    padding: 20px;
    margin: 25px;
    width:500px;
    cursor: pointer;
    background-color:skyblue;
    border-top-left-radius : 30px;
    border-bottom-right-radius : 30px;
    transition: all 0.2s;    
    overflow-x: auto;
    overflow-y: auto;
  }
  .post:hover{
    opacity: 0.8;
  }
</style>