const express = require("express");
const {graphqlHTTP} = require("express-graphql");
const schema = require("./schema.js");

const app = express();

app.use('/graphql', graphqlHTTP({
    schema,
    graphiql:true
}));


const PORT = process.env.PORT || 4040

app.listen(PORT, ()=> console.log(`Server listen on ${PORT}`));