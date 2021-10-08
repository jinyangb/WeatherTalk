// for heroku API
// const API_URL = process.env.VUE_APP_API_URL

export const BASE_URL =
  process.env.NODE_ENV === 'production'
    ? `https://weathertalk.herokuapp.com/`
    : 'http://localhost:5000'
//
