<template>
  <div class="home">
      <form @submit.prevent="name">
        <input name="name" type="text" placeholder="Name" :value="name" @change="handleChange"/>
        <input name="comment" type="text" placeholder="Comment" :value="comment" @change="handleChange"/>
        <input name="location" type="text" placeholder="Location" :value="location" @change="handleChange"/>
        <button @click="submit" :disabled="!name" >Submit</button>
      </form>

    <WeatherPost />
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import WeatherPost from '../components/WeatherPost.vue'
export default {
  name: 'Home',
  components: {
    WeatherPost
  },
  data: ()=> ({
    name: '',
    comment: '',
    lcoation: ''

  }),
  methods: {
    handleChange(event) {
      this.name= event.target.value
      console.log(event)
    },
  }
}
</script>

<style scoped>
.modal {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.content-wrapper {
  border: 1px solid #757575;
  height: 50%;
  width: 50%;
  border-radius: 6px;
  border: 2px solid;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  background-color: #fafafa;
}

.content-wrapper,
form {
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-wrapper {
  flex-direction: column;
}

input,
button {
  padding: 0.5em 1.2em;
  border-radius: 6px;
  border: 2px solid transparent;
  transition: all 0.2s ease;
}

.error {
  border-color: #e57373;
}

.success {
  border-color: #a5d6a7;
}

input {
  border: 2px solid #757575;
  outline: none;
}

button {
  margin-left: 1em;
  cursor: pointer;
}

button:not(:disabled) {
  background-color: #64b5f6;
}

h4 {
  margin-top: 2em;
}

.bold {
  font-weight: 800;
}

.green {
  color: #a5d6a7;
}
.red {
  color: #e57373;
}
</style>
