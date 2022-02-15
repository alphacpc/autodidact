import React from 'react'

const Launch = ({launch, index}) => {

    console.log(launch)

    return (
        <div className='divLaunch' key={index}>
            <div className='divLaunchInf'>
                <h2>Mission : <span style={{color:"red"}}>{launch.mission_name}</span></h2>
                <p>{new Date(launch.launch_date_local).toLocaleDateString()}</p>
            </div>
            <button>Show more</button>
        </div>
    )
}

export default Launch