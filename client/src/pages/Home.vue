<template>
  <div class="home">
      <section class="container" v-if="this.currentWeather">
        <h3>Your Current Weather</h3>
        <div class="current-weather">
          <h4>{{ Math.ceil(this.currentWeather.feels_like) }}&#176;</h4>
          <p>{{ this.currentWeather.weather[0].description }}</p>
          <img :src="`http://openweathermap.org/img/wn/${this.currentWeather.weather[0].icon}@2x.png`" />
        </div>
      </section>
      <section v-else>
        <h3>No Current Weather For data for your location...</h3>
      </section>
      <form @submit.prevent="submitPost">
        <input maxlength="80" name="name" type="text" placeholder="Name" :value="input.name" @change="handleChange"/>
        <input maxlength="80" name="location" type="text" placeholder="Location" :value="input.location" @change="handleChange"/>
        <textarea maxlength="255" rows="4" cols="50" class="comment" name="comment" type="text" placeholder="Comment" :value="input.comment" @change="handleChange"/>
        <button :disabled="!input.name" >Submit</button>
      </form>
    <div v-if="this.posts" class="post-container">
      <WeatherPost 
        v-for="post in posts"
        :key="post.id"
        :post="post"
        @deletePost="deletePost"
      /> 
    </div>
    <div v-else class="post-container">
      <h3>No Weather Posts :(</h3>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import WeatherPost from '../components/WeatherPost.vue'
const API_KEY = process.env.VUE_APP_WEATHER_KEY
import {BASE_URL} from '../globals'

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
          `${BASE_URL}/posts`, data
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
      try {
        const res = await axios.get(
          `${BASE_URL}/posts`
        )
        this.posts = res.data
      } catch (error) {
        console.log(error)
      }
    },
    async deletePost(postId){
      try {
      const res = await axios.delete(
          `${BASE_URL}/posts/${postId}`
        )
      const index = this.posts.indexOf(res.data["payload"])
      this.posts.splice(index,1)
      } catch (error) {
        console.log(error)
      }
    },
  },
  
}
</script>

<style scoped>
.container {
  background-color: #c2e59c; 
  background: -webkit-linear-gradient(to right, #c2e59c, #64b3f4); 
  background: linear-gradient(to right, #c2e59c, #64b3f4);
  border-top-left-radius : 30px;
  border-bottom-right-radius : 30px;
  width: 300px;
  justify-content:center;
  margin: 40px;
}

.home{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h3 {
  font-size: 1.5em;
}
.current-weather > h4 {
  font-size: 1.5em;
}
.current-weather > p {
  font-size: 1.4em;
}


form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}


input,
button,
textarea {
  padding: 0.5em 1.2em;
  border-radius: 6px;
  border: 2px solid transparent;
  transition: all 0.2s ease;
  margin: .2em;
}

input,
textarea {
  border: 2px solid #757575;
  outline: none;
  width: 500px;
}

button {
  margin-left: 1em;
  cursor: pointer;
}

button:not(:disabled) {
  background-color: #64b5f6;
}

.post-container {
  display: flex;
  flex-flow: column-reverse;
  align-items: center;
}
</style>
