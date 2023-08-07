'use client'

import React, { useState, FC,useRef } from 'react';
import CameraDiv from './camera/CameraDiv';
import FoodInfoDiv from './foodInfoDiv/foodInfoDiv';

export default function Page() {
  let [DataURL, setDataURL] = useState<string>('');
  return (
    <div className='main'>
      <CameraDiv onDataURLChange={data => setDataURL(data)} />
      <FoodInfoDiv DataURL={DataURL}/>
    </div>
  );
}