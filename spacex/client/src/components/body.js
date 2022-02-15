import React, {useEffect, useState} from 'react';

import Loader from "./loader";
import Launch from "./launch";

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


    if (loading){
        return <Loader/>
    }
    else{
        if(launches){
            return <div className='body'>
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

                    <div className="divSearch">
                        <input type="search" placeholder='Recherche...'/>
                    </div>

                    <div className='divLaunches'>

                        {
                            launches.map((item,index) => <Launch launch={item} index={index}/> )
                        }
                    </div>
                </div>
            
        }
    }

}

export default Body