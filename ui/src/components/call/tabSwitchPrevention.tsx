import React, { useEffect, useState } from "react";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";

interface TabSwitchWarningProps {
  isEnded: boolean;
};

const useTabSwitchPrevention = () => {
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [tabSwitchCount, setTabSwitchCount] = useState(0);

  useEffect(() => {
    const handleVisibilityChange = () => {
      if (document.hidden) {
        setIsDialogOpen(true);
        setTabSwitchCount((prev) => prev + 1);
      }
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);

    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, []);

  const handleUnderstand = () => {
    setIsDialogOpen(false);
  };

  return { isDialogOpen, tabSwitchCount, handleUnderstand };
};

function TabSwitchWarning({ isEnded }: TabSwitchWarningProps) {
  const { isDialogOpen, handleUnderstand } = useTabSwitchPrevention();

  if (isEnded) return null;

  return (
    <AlertDialog open={isDialogOpen}>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>Warning: Tab Switching</AlertDialogTitle>
          <AlertDialogDescription>
            Switching tabs may degrade your interview performance. Tab switching
            is tracked.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogAction
            className="bg-indigo-400 hover:bg-indigo-600 text-white"
            onClick={handleUnderstand}
          >
            I understand
          </AlertDialogAction>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  );
}

export { TabSwitchWarning, useTabSwitchPrevention };
