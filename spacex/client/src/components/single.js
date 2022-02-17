import React, {useEffect} from 'react';
import { useParams } from "react-router-dom";
import { useQuery } from "@apollo/client";

import {LAUNCH_ID} from "../GraphQL/Queries";


const Single = () => {

  let { flightNum } = useParams()
  flightNum = parseInt(flightNum);

  

  const { loading, error, data } = useQuery(LAUNCH_ID, {
    variables: { flight_number: flightNum },
  });


  useEffect( () => {
    
    console.log(data, "mes donnees dans single")

  },[data])


  console.log(flightNum,"Le parametre passer au url")

  return (
    <div>
      <h2>Hello world</h2>
    </div>
  )
}

export default Single