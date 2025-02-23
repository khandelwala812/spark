import { useEffect, useState } from "react";
import Image from "next/image";
import { Card, CardContent, CardTitle } from "@/components/ui/card";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { Trash } from "lucide-react";
import axios from "axios";
import MiniLoader from "@/components/loaders/mini-loader/miniLoader";
import { InterviewerService } from "@/services/interviewers.service";

interface Props {
  name: string | null;
  id: string;
  // url: string;
  // readableSlug: string;
}

const base_url = process.env.NEXT_PUBLIC_LIVE_URL;

function InterviewCard({ name, id }: Props) {
  const [copied, setCopied] = useState(false);
  const [responseCount, setResponseCount] = useState<number | null>(null);
  const [isFetching, setIsFetching] = useState(false);

  // const copyToClipboard = () => {
  //   navigator.clipboard
  //     .writeText(base_url + `/call/${id}`)
  //     .then(
  //       () => {
  //         setCopied(true);
  //         toast.success(
  //           "The link to your interview has been copied to your clipboard.",
  //           {
  //             position: "bottom-right",
  //             duration: 3000,
  //           },
  //         );
  //         setTimeout(() => {
  //           setCopied(false);
  //         }, 2000);
  //       },
  //       (err) => {
  //         console.log("failed to copy", err.mesage);
  //       },
  //     );
  // };

  return (
    <a
      href={`/interviews/${id}`}
      style={{
        pointerEvents: isFetching ? "none" : "auto",
        cursor: isFetching ? "default" : "pointer",
      }}
    >
      <Card className="relative p-0 mt-4 inline-block cursor-pointer h-60 w-56 ml-1 mr-3 rounded-xl shrink-0 overflow-hidden shadow-md">
        <CardContent className={`p-0 ${isFetching ? "opacity-60" : ""}`}>
          <div className="w-full h-40 overflow-hidden bg-indigo-600 flex items-center text-center">
            <CardTitle className="w-full mt-3 mx-2 text-white text-lg">
              {name}
              {isFetching && (
                <div className="z-100 mt-[-5px]">
                  <MiniLoader />
                </div>
              )}
            </CardTitle>
          </div>
          <div className="flex flex-row items-center mx-4 ">
            <div className="w-full overflow-hidden">
              <Image
                src={'/interviewers/Lisa.png'}
                alt="Picture of the interviewer"
                width={70}
                height={70}
                className="object-cover object-center"
              />
            </div>
          </div>
          <div className="absolute top-2 right-2">
            <Button
              className="text-xs text-indigo-600 px-1 h-6"
              variant={"secondary"}
              onClick={(event) => {
                event.stopPropagation();
                event.preventDefault();
              }}
            >
              {/* {copied ? <CopyCheck size={16} /> : <Copy size={16} />} */}
              <Trash size={16} />
            </Button>
          </div>
        </CardContent>
      </Card>
    </a>
  );
}

export default InterviewCard;
