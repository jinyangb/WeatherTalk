<template>
  <section>
    <h3>Current Weather</h3>
    <div>
      <!-- <h4>{{ Math.ceil(currentWeather.feels_like) }}&#176;</h4>
      <p>{{ currentWeather.weather[0].description }}</p>
      <img :src="generateIconUrl(currentWeather.weather[0].icon)" /> -->
    </div>
  </section>
</template>

<script>
export default {
  name: 'WeatherPost',
  props: {

  },
  methods: {
    generateIconUrl(ico) {
      return `http://openweathermap.org/img/wn/${ico}@2x.png`
    },
        enterName(e) {
      this.$emit('handleName', e.target.value, e.keyCode)
    },
        submitName() {
      this.$emit('submitName')
    }
  }
}
</script>
