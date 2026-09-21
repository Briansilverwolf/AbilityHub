"use client"

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { toast } from '@/components/ui/toast'

export default function UploadCVPage() {
  const [file, setFile] = useState<File | null>(null)
  const [status, setStatus] = useState<'idle' | 'uploading' | 'extracting' | 'reviewing' | 'privacy' | 'success'>('idle')
  const [error, setError] = useState<string | null>(null)

  // Extracted data (simulated)
  const [skills, setSkills] = useState<string[]>([])
  const [experience, setExperience] = useState<Array<{ company: string; role: string; start: string; end: string; description: string }>>([])
  const [education, setEducation] = useState<Array<{ institution: string; degree: string; field: string; start: string; end: string }>>([])
  const [qualifications, setQualifications] = useState<string[]>([])

  // Privacy settings
  const [visibility, setVisibility] = useState<'public' | 'connections' | 'private'>('connections')

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0]
    if (!selectedFile) {
      setFile(null)
      setStatus('idle')
      return
    }

    // Validate file type
    const allowedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain']
    if (!allowedTypes.includes(selectedFile.type)) {
      setError('Unsupported file type. Please upload PDF, DOC, DOCX, or TXT.')
      setFile(null)
      return
    }

    // Validate size (<=5 MB)
    const maxSize = 5 * 1024 * 1024 // 5 MB
    if (selectedFile.size > maxSize) {
      setError('File size exceeds 5 MB limit.')
      setFile(null)
      return
    }

    setFile(selectedFile)
    setError(null)
    setStatus('uploading')
  }

  const simulateExtraction = async () => {
    setStatus('extracting')
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1500))

    // Simulate extracted data (in real app, this would come from backend/service)
    setSkills(['JavaScript', 'React', 'Node.js', 'SQL', 'Git'])
    setExperience([
      { company: 'Tech Corp', role: 'Senior Frontend Engineer', start: '2020-03', end: 'Present', description: 'Led development of customer-facing web applications using React and TypeScript.' },
      { company: 'StartupXYZ', role: 'Full Stack Developer', start: '2018-06', end: '2020-02', description: 'Built RESTful APIs and integrated third-party services.' }
    ])
    setEducation([
      { institution: 'University of Example', degree: 'Bachelor of Science', field: 'Computer Science', start: '2014-09', end: '2018-05' },
      { institution: 'Online Academy', degree: 'Certification', field: 'AWS Solutions Architect', start: '2021-01', end: '2021-06' }
    ])
    setQualifications(['AWS Certified Solutions Architect', 'Scrum Master Certification'])

    setStatus('reviewing')
  }

  const handleAddSkill = (skill: string) => {
    if (skill.trim() && !skills.includes(skill.trim())) {
      setSkills([...skills, skill.trim()])
    }
  }

  const handleRemoveSkill = (skillToRemove: string) => {
    setSkills(skills.filter(s => s !== skillToRemove))
  }

  const handleSubmit = async () => {
    setStatus('privacy')
    // In reality, we would send data to backend here
    await new Promise(resolve => setTimeout(resolve, 1000))
    setStatus('success')
    toast.success('Profile created successfully and made searchable!')
    // Reset after a short delay
    setTimeout(() => {
      setFile(null)
      setStatus('idle')
      setSkills([])
      setExperience([])
      setEducation([])
      setQualifications([])
      setVisibility('connections')
    }, 2000)
  }

  if (status === 'success') {
    return (
      <div className="min-h-[calc(100vh-4.5rem)] flex items-center justify-center px-4 py-8 sm:px-6 lg:px-8">
        <Card className="w-full max-w-md">
          <CardHeader className="mb-6">
            <CardTitle className="text-2xl font-bold text-blue-600">
              Profile Created
            </CardTitle>
            <CardDescription className="text-muted-foreground">
              Your CV has been processed and your profile is now searchable.
            </CardDescription>
          </CardHeader>
          <CardContent className="text-center">
            <p className="mb-4">
              You can now <a href="/" className="underline text-blue-600">return to home</a> or <a href="/login" className="underline text-blue-600">log in</a>.
            </p>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="min-h-[calc(100vh-4.5rem)] flex items-center justify-center px-4 py-8 sm:px-6 lg:px-8">
      <Card className="w-full max-w-2xl">
        <CardHeader className="mb-6">
          <CardTitle className="text-2xl font-bold text-blue-600">
            Upload CV & Create Searchable Profile
          </CardTitle>
          <CardDescription className="text-muted-foreground">
            Upload your CV to automatically extract qualifications and create a discoverable profile.
          </CardDescription>
        </CardHeader>
        <CardContent>
          {status === 'idle' && (
            <form className="space-y-6" onSubmit={(e) => e.preventDefault()}>
              <div>
                <Label htmlFor="cv-upload" className="text-blue-600 font-medium">
                  Select CV File
                </Label>
                <Input
                  id="cv-upload"
                  type="file"
                  accept=".pdf,.doc,.docx,.txt"
                  className="mt-2 block w-full text-sm text-muted-foreground file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-blue-50 file:text-sm file:font-medium file:text-blue-600 hover:file:bg-blue-100"
                  disabled={status === 'uploading' || status === 'extracting' || status === 'reviewing' || status === 'privacy'}
                  onChange={handleFileChange}
                />
                {error && <p className="mt-2 text-sm text-destructive">{error}</p>}
                {file && (
                  <p className="mt-2 text-sm text-muted-foreground">
                    Selected: {file.name} ({((file.size / 1024 / 1024).toFixed(2))} MB)
                  </p>
                )}
              </div>

              {!error && file && (
                <Button
                  onClick={simulateExtraction}
                  className="w-full bg-blue-600 hover:bg-blue-700 disabled:opacity-50"
                  disabled={status === 'uploading' || status === 'extracting'}
                >
                  {status === 'uploading' ? 'Uploading...' : 'Process CV'}
                </Button>
              )}
            </form>
          )}

          {status === 'extracting' && (
            <div className="text-center py-8">
              <p className="mb-4">Extracting information from your CV...</p>
              {/* Simple loading indicator */}
              <div className="h-2 w-32 bg-blue-200 rounded-full overflow-hidden">
                <div className="h-2 w-1/3 bg-blue-600 transition-all duration-1000" style={{ width: '33%' }}></div>
              </div>
            </div>
          )}

          {(status === 'reviewing' || status === 'privacy') && file && (
            <>
              <div className="space-y-6">
                {/* Skills */}
                <div>
                  <Label htmlFor="skills" className="text-blue-600 font-medium mb-2">
                    Skills
                  </Label>
                  <div className="flex flex-wrap gap-2 mb-4">
                    {skills.map((skill, idx) => (
                      <span key={idx} className="bg-blue-100 text-blue-800 text-xs font-medium px-3 py-1 rounded-full">
                        {skill}
                        <button
                          onClick={() => handleRemoveSkill(skill)}
                          className="ml-2 text-blue-500 hover:text-blue-700"
                          aria-label={`Remove skill ${skill}`}
                        >
                          ×
                        </button>
                      </span>
                    ))}
                    <Input
                      id="skills-input"
                      placeholder="Add a skill..."
                      className="flex-1 min-w-[80px]"
                      onKeyPress={(e) => {
                        if (e.key === 'Enter') {
                          handleAddSkill(e.currentTarget.value)
                          e.currentTarget.value = ''
                        }
                      }}
                    />
                  </div>
                </div>

                {/* Experience */}
                <div>
                  <Label htmlFor="experience" className="text-blue-600 font-medium mb-2">
                    Experience
                  </Label>
                  {experience.map((exp, idx) => (
                    <div key={idx} className="border border-blue-200 rounded-lg p-4 mb-4">
                      <div className="flex justify-between items-start mb-2">
                        <h3 className="font-semibold text-blue-600">{exp.role}</h3>
                        <span className="text-sm text-muted-foreground">{exp.company}</span>
                      </div>
                      <p className="text-sm text-muted-foreground mb-2">
                        {exp.start} – {exp.end || 'Present'}
                      </p>
                      <Textarea
                        value={exp.description}
                        onChange={(e) => {
                          const newExp = [...experience]
                          newExp[idx] = { ...newExp[idx], description: e.target.value }
                          setExperience(newExp)
                        }}
                        className="w-full min-h-[60px] resize-none border border-blue-200 rounded-lg px-3 py-2"
                        placeholder="Brief description of responsibilities and achievements"
                      />
                    </div>
                  ))}
                  <Button
                    variant="outline"
                    onClick={() => {
                      setExperience([...experience, { company: '', role: '', start: '', end: '', description: '' }])
                    }}
                    className="mt-2"
                  >
                    Add Experience
                  </Button>
                </div>

                {/* Education */}
                <div>
                  <Label htmlFor="education" className="text-blue-600 font-medium mb-2">
                    Education
                  </Label>
                  {education.map((edu, idx) => (
                    <div key={idx} className="border border-blue-200 rounded-lg p-4 mb-4">
                      <div className="flex justify-between items-start mb-2">
                        <h3 className="font-semibold text-blue-600">{edu.degree}</h3>
                        <span className="text-sm text-muted-foreground">{edu.institution}</span>
                      </div>
                      <p className="text-sm text-muted-foreground mb-2">
                        {edu.field}
                      </p>
                      <p className="text-sm text-muted-foreground mb-2">
                        {edu.start} – {edu.end}
                      </p>
                    </div>
                  ))}
                  <Button
                    variant="outline"
                    onClick={() => {
                      setEducation([...education, { institution: '', degree: '', field: '', start: '', end: '' }])
                    }}
                    className="mt-2"
                  >
                    Add Education
                  </Button>
                </div>

                {/* Qualifications */}
                <div>
                  <Label htmlFor="qualifications" className="text-blue-600 font-medium mb-2">
                    Qualifications / Certifications
                  </Label>
                  <div className="flex flex-wrap gap-2 mb-4">
                    {qualifications.map((qual, idx) => (
                      <span key={idx} className="bg-blue-100 text-blue-800 text-xs font-medium px-3 py-1 rounded-full">
                        {qual}
                        <button
                          onClick={() => {
                            const newQuals = [...qualifications]
                            newQuals.splice(idx, 1)
                            setQualifications(newQuals)
                          }}
                          className="ml-2 text-blue-500 hover:text-blue-700"
                          aria-label={`Remove qualification ${qual}`}
                        >
                          ×
                        </button>
                      </span>
                    ))}
                    <Input
                      id="qual-input"
                      placeholder="Add a qualification..."
                      className="flex-1 min-w-[80px]"
                      onKeyPress={(e) => {
                        if (e.key === 'Enter') {
                          handleAddSkill(e.currentTarget.value) // reuse same function for simplicity
                          e.currentTarget.value = ''
                        }
                      }}
                    />
                  </div>
                </div>
              </div>

              {status === 'privacy' && (
                <div className="mt-6">
                  <Label htmlFor="visibility" className="text-blue-600 font-medium mb-2">
                    Profile Visibility
                  </Label>
                  <div className="space-y-2">
                    <label className="flex items-center gap-3">
                      <input
                        type="radio"
                        name="visibility"
                        value="public"
                        checked={visibility === 'public'}
                        onChange={(e) => setVisibility(e.target.value as any)}
                        className="h-4 w-4 text-blue-600"
                      />
                      <span>Public (visible to everyone)</span>
                    </label>
                    <label className="flex items-center gap-3">
                      <input
                        type="radio"
                        name="visibility"
                        value="connections"
                        checked={visibility === 'connections'}
                        onChange={(e) => setVisibility(e.target.value as any)}
                        className="h-4 w-4 text-blue-600"
                      />
                      <span>Connections only (visible to your network)</span>
                    </label>
                    <label className="flex items-center gap-3">
                      <input
                        type="radio"
                        name="visibility"
                        value="private"
                        checked={visibility === 'private'}
                        onChange={(e) => setVisibility(e.target.value as any)}
                        className="h-4 w-4 text-blue-600"
                      />
                      <span>Private (only visible to you)</span>
                    </label>
                  </div>
                </div>
              )}

              <div className="mt-6 flex justify-end space-x-4">
                {status === 'reviewing' && (
                  <Button
                    onClick={() => setStatus('privacy')}
                    className="bg-blue-600 hover:bg-blue-700"
                  >
                    Continue to Privacy
                  </Button>
                )}
                {status === 'privacy' && (
                  <>
                    <Button
                      onClick={() => setStatus('reviewing')}
                      variant="outline"
                    >
                      Back to Review
                    </Button>
                    <Button
                      onClick={handleSubmit}
                      className="bg-blue-600 hover:bg-blue-700"
                    >
                      Create Profile
                    </Button>
                  </>
                )}
              </div>
            </>
          )}
        </CardContent>
      </Card>
    </div>
  )
}