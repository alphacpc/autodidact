import React from 'react'

const Launch = ({launch, index}) => {

    return (
        <div className='divLaunch' key={launch.flight_number}>
            <div className='divLaunchInf'>
                <h2>Mission : <span className={launch.launch_success ? 'isSuccess': 'isFailure'}>{launch.mission_name}</span></h2>
                <p>{new Date(launch.launch_date_local).toLocaleDateString()}</p>
            </div>
            <a href={`/single/${launch.flight_number}`}>Show more</a>
        </div>
    )
}

export default Launch