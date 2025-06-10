import { createFileRoute } from "@tanstack/react-router";
import LoginForm from "@/components/forms/Login";

export const Route = createFileRoute("/Login")({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className="flex flex-col items-center justify-center w-1/2">
      <LoginForm />
    </div>
  );
}
