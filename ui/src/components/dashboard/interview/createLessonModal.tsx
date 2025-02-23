import React, { useEffect, useState, useRef } from "react";

interface Props {
  open: boolean;
  setOpen: (open: boolean) => void;
  videoSrc: string; // Prop to receive the video source
}

function CreateLessonModal({ open, setOpen, videoSrc }: Props) {
    const videoRef = useRef<HTMLVideoElement | null>(null);

    useEffect(() => {
        if (videoRef.current) {
          if (open) {
              videoRef.current.play();
              videoRef.current.volume = 1.0;
          } else {
            videoRef.current.pause();
            videoRef.current.currentTime = 0;
          }
        }
    }, [open]);

  return (
    <div className="modal-content w-full max-w-[50rem] h-0 pb-[56.25%]">
        <div className="aspect-video mt-6">
            <video ref={videoRef} controls className="h-full w-full">
                <source src={videoSrc} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
        </div>
    </div>
  );
}

export default CreateLessonModal;
