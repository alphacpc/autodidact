const express = require("express");
const cors = require("cors");
const {graphqlHTTP} = require("express-graphql");
const schema = require("./schema.js");

const app = express();

//MIDDLEWARE CORS
app.use(cors);

app.use('/graphql', graphqlHTTP({
    schema,
    graphiql:true
}));


const PORT = process.env.PORT || 4040

app.listen(PORT, ()=> console.log(`Server listen on ${PORT}`));