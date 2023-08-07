

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
        <div className="p-6 bg-white rounded-xl shadow-xl dark:bg-gray-800 max-w-cardSize w-full">
            <h4 className="text-2xl font-bold dark:text-white">음식 성분 결과</h4>
            
        </div>
    );
};

export default FoodInfoDiv;

