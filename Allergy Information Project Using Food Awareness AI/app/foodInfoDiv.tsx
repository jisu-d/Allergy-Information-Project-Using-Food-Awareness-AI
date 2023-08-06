

import React, { FC, useEffect, useState } from 'react';

interface ifoodInfoDiv{
    DataURL:string;
}

const FoodInfoDiv: FC<ifoodInfoDiv> = ({DataURL}) => {
    let [sliceDataURL, setSliceDataURL] = useState<string>('');
    
    useEffect(() => {
        if (DataURL !== ''){
            setSliceDataURL(DataURL.slice(DataURL.indexOf(',') + 1))
        } 
    }, [DataURL]);
    return (
        <>
            {}
        </>
    );
};

export default FoodInfoDiv;

