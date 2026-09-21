"use client"

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Label } from '@/components/ui/label';
import { Toast, ToastAction, ToastDescription, ToastTitle, Toaster, toast } from '@/components/ui/toast';

export default function ProfilePage() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [bio, setBio] = useState('');
  const [avatarUrl, setAvatarUrl] = useState<string | null>(null);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Here you would typically send the data to an API
    console.log('Form submitted:', { name, email, bio, role: 'user', avatarUrl });
    toast.success('Profile created successfully!');
    // Reset form
    setName('');
    setEmail('');
    setBio('');
    setAvatarUrl(null);
  };

  const handleAvatarChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setAvatarUrl(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="min-h-[calc(100vh-4.5rem)] flex items-center justify-center px-4 py-8 sm:px-6 lg:px-8">
      <Card className="w-full max-w-md">
        <CardHeader className="mb-6">
          <CardTitle className="text-2xl font-bold text-blue-600">
            Create Profile
          </CardTitle>
          <CardDescription className="text-muted-foreground">
            Fill in your details to create a new profile.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="flex items-center justify-center mb-6">
              <div className="relative h-24 w-24 bg-blue-50 rounded-full p-1">
                <Avatar
                  className="h-24 w-24 bg-blue-600"
                  src={avatarUrl}
                  onClick={() => document.getElementById('avatar-upload')?.click()}
                  alt="Avatar"
                >
                  {!avatarUrl && <AvatarFallback className="text-white">{name?.charAt(0)?.toUpperCase() ?? '?'}</AvatarFallback>}
                </Avatar>
                <input
                  id="avatar-upload"
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleAvatarChange}
                />
              </div>
            </div>

            <div className="space-y-4">
              <div>
                <Label htmlFor="name" className="text-blue-600 font-medium">
                  Name
                </Label>
                <Input
                  id="name"
                  placeholder="Enter your full name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                  className="border-blue-200 focus:border-blue-500 focus:ring-blue-500"
                />
              </div>

              <div>
                <Label htmlFor="email" className="text-blue-600 font-medium">
                  Email
                </Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="Enter your email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="border-blue-200 focus:border-blue-500 focus:ring-blue-500"
                />
              </div>

              <div>
                <Label htmlFor="bio" className="text-blue-600 font-medium">
                  Bio
                </Label>
                <Textarea
                  id="bio"
                  placeholder="Tell us about yourself"
                  value={bio}
                  onChange={(e) => setBio(e.target.value)}
                  className="min-h-[80px] border-blue-200 focus:border-blue-500 focus:ring-blue-500"
                />
              </div>
            </div>

            <Button type="submit" className="w-full bg-blue-600 hover:bg-blue-700">
              Create Profile
            </Button>
          </form>
        </CardContent>
      </Card>

      <Toaster />
    </div>
  );
}