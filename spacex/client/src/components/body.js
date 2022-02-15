import React, {useEffect, useState} from 'react';

import Loader from "./loader"

import { useQuery } from "@apollo/client";
import {LAUNCHES_QUERIES} from "../GraphQL/Queries";


const Body = () => {

    const {loading, data} = useQuery(LAUNCHES_QUERIES);
    const [launches, setLaunches] = useState([])


    useEffect(() => {
        
        if(data){
            setLaunches(data.launches)
        }

    }, [data])

    console.log(launches)

    return loading? <Loader/> : (
        <div className='body'>
        <h1>Launches</h1>
    
        <div className='divLegend'>
            <div className='divLegendItem'>
                <span id="success"></span>
                <p>Success</p>
            </div>
            <div className='divLegendItem'>
                <span id="failure"></span>
                <p>Failure</p>
            </div>
        </div>

        <div className='divLaunches'>
            <div className='divLaunch'>
                <div className='divLaunchInf'>
                    <h2>Mission : <span style={{color:"red"}}>FalconSat</span></h2>
                    <p>2006-03-24T22:30:00</p>
                </div>
                <button>Show more</button>
            </div>

            <div className='divLaunch'>
                <div className='divLaunchInf'>
                    <h2>Mission : <span style={{color:"red"}}>FalconSat</span></h2>
                    <p>2006-03-24T22:30:00</p>
                </div>
                <button>Show more</button>
            </div>

            <div className='divLaunch'>
                <div className='divLaunchInf'>
                    <h2>Mission : <span style={{color:"red"}}>FalconSat</span></h2>
                    <p>2006-03-24T22:30:00</p>
                </div>
                <button>Show more</button>
            </div>
        </div>

    </div>
  )
}

export default Body