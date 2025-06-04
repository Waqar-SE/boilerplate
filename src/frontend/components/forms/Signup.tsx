import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

const Signup = () => {
  return (
    <div className="flex flex-col gap-2 w-1/4 p-4 shadow-xl rounded-lg">
      <div className="flex gap-2">
        <div>
          <Label>First name</Label>
          <Input />
        </div>
        <div>
          <Label>Last name</Label>
          <Input />
        </div>
      </div>
      <div>
        <Label>Email</Label>
        <Input />
      </div>
      <div>
        <Label>Phone</Label>
        <Input />
      </div>
      <div>
        <Label>Secondary Phone</Label>
        <Input />
      </div>
      <div>
        <Label>Password</Label>
        <Input />
      </div>
      <div>
        <Label>Confirm Password</Label>
        <Input />
      </div>
      <div className="flex gap-2">
        <div>
          <Label>Company Name</Label>
          <Input />
        </div>
        <div>
          <Label>Address</Label>
          <Input />
        </div>
      </div>
    </div>
  );
};

export default Signup;
