import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Separator } from "@/components/ui/separator";
import { Button } from "@/components/ui/button";
import { Link } from "@tanstack/react-router";

const Signup = () => {
  return (
    <form className="flex flex-col gap-2">
      <h1 className="text-2xl font-bold mb-8">Let's get you an account</h1>

      <div className="flex gap-2">
        <div>
          <Label>First name</Label>
          <Input placeholder="John" />
        </div>
        <div>
          <Label>Last name</Label>
          <Input placeholder="Doe" />
        </div>
      </div>
      <div>
        <Label>Email</Label>
        <Input placeholder="ping@brimrix.com" />
      </div>
      <div>
        <Label>Phone</Label>
        <Input placeholder="+923338693455" />
      </div>
      <div>
        <Label>Secondary Phone</Label>
        <Input placeholder="052324234" />
      </div>
      <Separator className="my-5" />
      <div className="flex gap-2">
        <div>
          <Label>Company Name</Label>
          <Input placeholder="Brimrix" />
        </div>
        <div>
          <Label>Address</Label>
          <Input placeholder="Sialkot, Pakistan" />
        </div>
      </div>
      <Separator className="my-5" />
      <div>
        <Label>Password</Label>
        <Input type="password" placeholder="Password" />
      </div>
      <div>
        <Label>Confirm Password</Label>
        <Input type="password" placeholder="Retype password" />
      </div>
      <div className="mt-5">
        <Button type="submit" className="w-full">
          Signup
        </Button>
      </div>

      <div className="text-center text-sm">
        Already have an account? Let's&nbsp;
        <Link className="underline" to="/Login">
          Login
        </Link>
      </div>
    </form>
  );
};

export default Signup;
