

console.log('hi')

const fetch = require('node-fetch')

const getFromApi = base => endpoint => cb  => 
    console.log(`${base}/${endpoint}`) ||fetch(`${base}/${endpoint}`)
    .then( res => res.json())
    .then (data => cb(data))
   // .error(e => console.error(e))

const gh = getFromApi('https://api.github.comx')
const get = (x , key) => x[key]

const user_props = prop => gh('users')
    ( x => x.map( d =>  get (d, prop)  ) )

user_props('id').then(x => console.log(x)).catch( e => console.error("ERROR ->" + e))

const add = x => y => x+y

console.log(add(3)(4))


