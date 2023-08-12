
import './CameraDiv.css'
import React, { useState, useEffect, useRef, FC } from 'react';

interface iCameraDiv{
    onDataURLChange:(data:string) => void;
}

const CameraDiv: FC<iCameraDiv> = ({onDataURLChange}) => {
    const videoRef = useRef<HTMLVideoElement>(null);
    const canvasRef = useRef<HTMLCanvasElement>(null);

    let [btnType, setBtnType] = useState<string>('Take a picture');

    let [displayType, setdisplayType] = useState<{video:string, takeimg:string, btn:string, tempImg:string}>({video:'none', takeimg:'none', btn: 'none', tempImg: 'block'})

    let [dataUrl, setdataUrl] = useState<string>('')

    useEffect(() => {
        const constraints = { audio: false, video: true, facingMode: { exact: "environment" } }

        async function setupCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia(constraints);
                if (videoRef.current) {
                    videoRef.current.srcObject = stream;
                }
            } catch (error) {
                console.error('Error accessing the camera:', error);
            }
        }

        setupCamera();
    }, []);

    const takePhoto = () => {
        if (videoRef.current && canvasRef.current) {
            const context = canvasRef.current.getContext('2d');
            if (context) {
                canvasRef.current.width = videoRef.current.videoWidth;
                canvasRef.current.height = videoRef.current.videoHeight;
                context.drawImage(videoRef.current, 0, 0, canvasRef.current.width, canvasRef.current.height);
                
                setdataUrl(canvasRef.current.toDataURL('image/jpeg'))
                
                onDataURLChange(canvasRef.current.toDataURL('image/jpeg'))
            }
        }
    };

    const onClick = () => {
        if (btnType == 'Again') {
            takePhoto()
            setBtnType('Take a picture')
            setdisplayType({video:'block', takeimg:'none' , btn: 'block' , tempImg: 'none'})
            
        } else if (btnType == 'Take a picture') {
            takePhoto()
            setBtnType('Again')
            setdisplayType({video:'none', takeimg:'block' , btn: 'block', tempImg: 'none'})
        }
    }

    const imgClick = () => {
        setdisplayType({video:'block', takeimg:'none' , btn: 'block', tempImg: 'none'})
    }

    return (
        <div className="p-6 bg-white rounded-xl shadow-xl dark:bg-gray-800 mb-6 flex flex-col max-w-cardSize w-full">
            <img onClick={imgClick} style={{ display: displayType.tempImg }} className="h-auto max-w-full rounded-lg" src="https://flowbite.com/docs/images/examples/image-3@2x.jpg" alt="image description"/>

            <div className='live-video-div' style={{ display: displayType.video }}>
                <video ref={videoRef} autoPlay playsInline muted className='w-full rounded-lg'/>
            </div>

            <div className='takePhoto-div' style={{ display: displayType.takeimg }}>
                <img src={dataUrl} alt="Captured" className='w-full rounded-lg'/>
            </div>

            {/* <button type="button" onClick={onClick} className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm  px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">{btnType}</button> */}
            <button type="button" onClick={onClick} style={{ display: displayType.btn }} className="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 mt-6 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 shadow-lg shadow-blue-500/50 dark:shadow-lg dark:shadow-blue-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center ">{btnType}</button>
            <canvas ref={canvasRef} style={{ display: 'none' }} />

        </div>
    );
};

export default CameraDiv;
