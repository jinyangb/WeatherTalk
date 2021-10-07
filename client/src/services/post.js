import Client from './api'

export const GetPosts = async () => {
  const res = await Client.get('/posts')
  return res.data
}

export const CreatePost = async data => {
  const res = await Client.post('/posts', data)
  return res.data
}

export const RemoveUser = async postId => {
  const res = await Client.delete(`/posts/${postId}`)
  return res.data
}
