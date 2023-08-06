

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
    //여기서 sliceDataURL에 저장된 데이터로 요청 보낼려고 합니다..
    return (
        <>
            {}
        </>
    );
};

export default FoodInfoDiv;

