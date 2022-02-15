import React from "react";

import { 
  ApolloClient, 
  InMemoryCache, 
  ApolloProvider, 
  HttpLink, 
  from } from "@apollo/client";
import { onError } from "@apollo/client/link/error"

import "./assets/css/app.css";

import Header from "./components/header";
import Body from "./components/body";
import Footer from "./components/footer";


const errorLink = onError(({graphErrors, networkError}) =>{
  if(graphErrors){
    graphErrors.map(({message, location, path}) => {
      alert(`Erreur avec GraphQL ${message}`);
    })
  }
})


const link = from([
  errorLink,
  new HttpLink({uri: "http://localhost:4040/graphql"})
])

const client = new ApolloClient({
  cache: new InMemoryCache,
  link: link
})

console.log("Hello client",client)

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <Header/>
        <Body/>
        <Footer/>
      </div>
    </ApolloProvider>

  );
}

export default App;
