<template>
  <div class="home">
      <section>
        <h3>Your Current Weather</h3>
        <div>
          <h4>{{ Math.ceil(this.currentWeather.feels_like) }}&#176;</h4>
          <p>{{ this.currentWeather.weather[0].description }}</p>
          <img :src="`http://openweathermap.org/img/wn/${this.currentWeather.weather[0].icon}@2x.png`" />
        </div>
      </section>
      <form @submit.prevent="submitPost">
        <input name="name" type="text" placeholder="Name" :value="input.name" @change="handleChange"/>
        <input name="comment" type="text" placeholder="Comment" :value="input.comment" @change="handleChange"/>
        <input name="location" type="text" placeholder="Location" :value="input.location" @change="handleChange"/>
        <button :disabled="!input.name" >Submit</button>
      </form>

    <WeatherPost />
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import WeatherPost from '../components/WeatherPost.vue'
const API_KEY = process.env.VUE_APP_WEATHER_KEY

export default {
  name: 'Home',
  components: {
    WeatherPost
  },
  data: ()=> ({
    input: {
      name: '',
      comment: '',
      location: ''
    },
    currentWeather: null,
    posts: []
  }),
  mounted: function(){
    navigator.geolocation.getCurrentPosition(async (position) => {
      await this.getCurrentWeather(position.coords)
    }),
    this.getPosts()
  },
  methods: {
    async submitPost() {
      const ico = this.currentWeather.weather[0].icon
      const data = {
        "name": this.input.name,
        "content": this.input.comment,
        "location": this.input.location,
        "temperature": Math.ceil(this.currentWeather.feels_like),
        "summary": this.currentWeather.weather[0].description,
        "icon_source": `http://openweathermap.org/img/wn/${ico}@2x.png`
      }
      try {
        const res = await axios.post(
          `http://localhost:5000/posts`, data
        )
        this.posts.push(res.data)
      } catch (error) {
        console.log(error)
      }
    },
    async getCurrentWeather(coords) {
      const res = await axios.get(
        `https://api.openweathermap.org/data/2.5/onecall?lat=${coords.latitude}&lon=${coords.longitude}&units=imperial&appid=${API_KEY}`
      )
      this.currentWeather = res.data.current
    },
    handleChange(event) {
      this.input[event.target.name] = event.target.value
    },
    async getPosts(){
      const res = await axios.get(
        `http://localhost:5000/posts`
      )
      this.posts = res.data
    },
  },
  
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
