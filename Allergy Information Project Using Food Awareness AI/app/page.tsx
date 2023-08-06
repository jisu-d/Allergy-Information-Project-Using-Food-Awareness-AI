'use client'

import React, { useState, FC } from 'react';
import CameraDiv from './CameraDiv';
import FoodInfoDiv from './foodInfoDiv';

export default function Page() {
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
}