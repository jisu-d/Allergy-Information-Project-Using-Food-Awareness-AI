import React, { useState, FC } from 'react';
import CameraDiv from './CameraComponent';
import FoodInfoDiv from './foodInfoDiv';

const App: FC = () => {
  let [DataURL, setDataURL] = useState<string>('');
  return (
    <div className='main'>
      <div>
        <CameraDiv onDataURLChange={data => setDataURL(data)} />
      </div>
      <div>
        <FoodInfoDiv DataURL={DataURL}/>
      </div>
    </div>
  );
};

export default App;
