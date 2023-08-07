
import './CameraDiv.css'
import React, { useState, useEffect, useRef, FC } from 'react';

interface iCameraDiv{
    onDataURLChange:(data:string) => void;
}

const CameraDiv: FC<iCameraDiv> = ({onDataURLChange}) => {
    const videoRef = useRef<HTMLVideoElement>(null);
    const canvasRef = useRef<HTMLCanvasElement>(null);

    let [btnType, setBtnType] = useState<string>('사진찍기');

    let [displayType, setdisplayType] = useState<{video:string, img:string}>({video:'block', img:'none'})

    let [dataUrl, setdataUrl] = useState<string>('')

    let [base64WebCamCapture, setbase64WebCamCapture] = useState<string>('')

    useEffect(() => {
        const constraints = { audio: false, video: { width: 1280, height: 720 } }

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
                
                let imgUrl = canvasRef.current.toDataURL('image/jpeg')

                setdataUrl(imgUrl);
                onDataURLChange(imgUrl);
                setbase64WebCamCapture(imgUrl.replace("data:image/jpeg;base64,",""));
            }
        }
    };

    const onClick = () => {
        if (btnType == '다시찍기') {
            takePhoto()
            setBtnType('사진찍기')
            setdisplayType({video:'block', img:'none'})
            
        } else if (btnType == '사진찍기') {
            takePhoto()
            setBtnType('다시찍기')
            setdisplayType({video:'none', img:'block'})
        }
    }
//.slice(dataUrl.indexOf(',') + 1)
    return (
        <>
            <div className='live-video-div' style={{display: displayType.video}}>
                <video ref={videoRef} autoPlay playsInline muted />
            </div>

            <div className='takePhoto-div' style={{display: displayType.img}}>
                <img src={dataUrl} alt="Captured" />
            </div>

            <button onClick={onClick} style={{fontSize: '100px'}}>{btnType}</button>
            <canvas ref={canvasRef} style={{ display: 'none' }} />
        </>
    );
};

export default CameraDiv;
