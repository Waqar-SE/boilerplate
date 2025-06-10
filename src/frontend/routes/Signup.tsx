import SignupForm from "@/components/forms/Signup";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/Signup")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="w-1/2 flex flex-column justify-center items-center">
      <div className="w-1/2">
        <SignupForm />
      </div>
    </div>
  );
}
