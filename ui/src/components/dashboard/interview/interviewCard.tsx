import { useEffect, useState } from "react";
import Image from "next/image";
import { Card, CardContent, CardTitle } from "@/components/ui/card";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { TrashIcon } from "lucide-react";
import axios from "axios";
import MiniLoader from "@/components/loaders/mini-loader/miniLoader";
import { InterviewerService } from "@/services/interviewers.service";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";
import { InterviewService } from "@/services/interviews.service";
import { useRouter } from "next/navigation";
import { useInterviews } from "@/contexts/interviews.context";
interface Props {
  name: string | null;
  id: string;
  // url: string;
  // readableSlug: string;
}

const base_url = process.env.NEXT_PUBLIC_LIVE_URL;

function InterviewCard({ name, id }: Props) {
  const router = useRouter();
  const { fetchInterviews } = useInterviews();
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

  const deleteInterview = async () => {
    await InterviewService.deleteInterview(id);
    await fetchInterviews()
    
    toast.success("Interview deleted successfully.", {
      position: "bottom-right",

      duration: 3000,
    });
  }

  return (
    // <a
    //   href={`/interviews/${id}`}
    //   style={{
    //     pointerEvents: isFetching ? "none" : "auto",
    //     cursor: isFetching ? "default" : "pointer",
    //   }}
    // >
      <Card className="relative p-0 mt-4 inline-block h-60 w-56 ml-1 mr-3 rounded-xl shrink-0 overflow-hidden shadow-md">
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
          <div className="flex flex-row w-full justify-center items-center space-x-8 mt-5">
              <Button
                className="bg-indigo-600 hover:bg-indigo-800 w-30"
                onClick={() => router.push(`/call/${id}`)}
              >
                Start
              </Button>
              <Button
                className="bg-indigo-600 hover:bg-indigo-800 w-30"
                onClick={() => router.push(`/interviews/${id}`)}
              >
                Analyze
              </Button>
          </div>
          <div className="absolute top-2 right-2">
            <AlertDialog>
              <AlertDialogTrigger>
                <Button
                    className="text-xs text-white px-1 h-6"
                >
                  <TrashIcon size={16} className="" />
                </Button>
              </AlertDialogTrigger>

              <AlertDialogContent>
                <AlertDialogHeader>
                  <AlertDialogTitle>Are you sure?</AlertDialogTitle>
                  <AlertDialogDescription>
                    This action cannot be undone. This will permanently
                    delete this interview.
                  </AlertDialogDescription>
                </AlertDialogHeader>

                <AlertDialogFooter>
                  <AlertDialogCancel>Cancel</AlertDialogCancel>

                  <AlertDialogAction
                    className="bg-indigo-600 hover:bg-indigo-800"
                    onClick={deleteInterview}
                  >
                    Continue
                  </AlertDialogAction>
                </AlertDialogFooter>
              </AlertDialogContent>
            </AlertDialog>
          </div>
        </CardContent>
      </Card>
    // </a>
  );
}

export default InterviewCard;
