import Image from "next/image"
import React, { useState } from "react";
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { PlayCircle } from "lucide-react"
import Modal from "@/components/dashboard/Modal";
import CreateLessonModal from "@/components/dashboard/interview/createLessonModal";

interface LessonCardProps {
  title: string
  description: string
  image: string
  videoSrc: string
}

export function CreateLessonCard({ title, description, image, videoSrc }: LessonCardProps) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <Card className="overflow-hidden">
        <div className="aspect-video relative">
          <Image src={image || "/placeholder.svg"} alt={title} fill className="object-cover" priority />
        </div>
        <CardHeader>
          <CardTitle className="line-clamp-1">{title}</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-sm text-muted-foreground line-clamp-2">{description}</p>
        </CardContent>
        <CardFooter>
          <Button 
              className="w-full cursor-pointer hover:scale-105 ease-in-out duration-300"
              onClick={() => setOpen(true)}
          >
            <PlayCircle className="mr-2 h-4 w-4" />
            Start Lesson
          </Button>
        </CardFooter>
      </Card>
      <Modal
        open={open}
        closeOnOutsideClick={false}
        onClose={() => {
          setOpen(false);
        }}
      >
        <CreateLessonModal open={open} setOpen={setOpen} videoSrc={videoSrc} />
      </Modal>
    </>
  )
}