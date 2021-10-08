<template>
  <section class="post">
    <div class="content">
    <div >
      <h4>{{ post.temperature }}&#176;</h4>
      <p>{{ post.summary  }}</p>
      <img :src="post.icon_source" />
    </div>
    <div>
      <h4>{{ post.name }}</h4>
      <h4>{{ post.location }}</h4>
      <p>{{ post.content }}</p>
    </div>
    </div>
    <div class = "date">
      <h4> {{post.created_at.slice(0,16)}} </h4>
    </div>
    <div class="delete-button-container">
      <button class="delete-button" @click="deletePost(post.id)">X</button>
    </div>
  </section>
</template>

<script>
export default {
  name: 'WeatherPost',
  props: {
    post: {}
  },
  methods: {
    deletePost(postId) {
      this.$emit('deletePost', postId)
    }
  }
}
</script>

<style scoped>
  .post {
    display: flex;
    flex-direction: column;
    border: 3px solid black;
    border-radius: 15px;
    justify-content:space-evenly;
    padding: 20px;
    margin: 25px;
    width:500px;
    cursor: pointer;
    background-color: #c2e59c; 
    background: -webkit-linear-gradient(to right, #c2e59c, #64b3f4); 
    background: linear-gradient(to right, #c2e59c, #64b3f4); 
    border-top-left-radius : 30px;
    border-bottom-right-radius : 30px;
    transition: all 0.2s;    
    overflow-x: auto;
    overflow-y: auto;
    font-weight: bold;
    color: black;
    /* background-image: url("https://i.imgur.com/PtlNNn0t.jpg"); */
  }
  .post:hover{
    opacity: 0.8;
  }
  .content {
    display: flex;
    justify-content:space-evenly;
    width:500px;
  }
  .date {
    display: flex; 
    justify-content:space-evenly;
    align-items: flex-start;
    height: 20px;
    padding: 5px;
  }
  .delete-button-container {
    position: relative;
    width: 20px;
    height: 20px;
  }
  .delete-button {
    background-color: black;
    border-radius: 5px;
    border: none;
    color: #64b3f4;
  }

</style>