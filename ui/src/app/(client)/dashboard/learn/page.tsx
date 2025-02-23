"use client";

import React, { useState, useEffect } from "react";
import { CreateLessonCard } from "@/components/dashboard/interview/createLessonCard";

const lessons = [
    {
      id: 1,
      title: "Tell me about yourself",
      description: 'Learn how to answer the most important question in the interview "Tell me about yourself"',
      image: "/learn/tell-me-about-yourself.png",
      videoSrc: "/learn/tell-me-about-yourself.mp4"
    },
    {
      id: 2,
      title: "Any Questions?",
      description: 'Learn how to structure and ask follow up questions near the end of the interview',
      image: "/learn/follow-up-questions.png",
      videoSrc: "/learn/follow-up-questions.mp4"
    },
  ]

function Learn() {
    return (
      <main className="p-8 pt-0 ml-12 mr-auto rounded-md">
        <div className="flex flex-col items-left">
          <div className="mb-6">
            <h2 className="mr-2 text-2xl font-semibold tracking-tight mt-8">Available Lessons</h2>
            <h3 className=" text-sm tracking-tight text-gray-600 font-medium ">Start learning with our curated lessons</h3>
          </div>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {lessons.map((lesson) => (
              <CreateLessonCard key={lesson.id} {...lesson} />
            ))}
          </div>
        </div>
      </main>
    );
}

export default Learn;