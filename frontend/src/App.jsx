import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { Search, Settings, Bell, Download, ExternalLink, Calendar, MapPin, Building, Star } from 'lucide-react'
import { motion, AnimatePresence } from 'framer-motion'
import './App.css'

function App() {
  const [jobs, setJobs] = useState([])
  const [filteredJobs, setFilteredJobs] = useState([])
  const [searchTerm, setSearchTerm] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [stats, setStats] = useState({
    total_scraped: 0,
    total_relevant: 0,
    sources_processed: 0,
    last_update: null
  })

  // Simulation de données pour la démonstration
  const mockJobs = [
    {
      id: 1,
      title: "Maître de Conférences en Sociologie des Cryptomonnaies",
      institution: "Université Paris-Saclay - Laboratoire PRINTEMPS",
      location: "Versailles, France",
      deadline: "2025-08-15",
      url: "https://example.com/job1",
      source: "Galaxie",
      keywords_match: ["crypto", "sociologie", "gouvernance"],
      relevance_score: 0.85,
      teaching: "Oui",
      language: "Français",
      found_date: "2025-06-18"
    },
    {
      id: 2,
      title: "Assistant Professor in Digital Political Economy",
      institution: "Sciences Po - Médialab",
      location: "Paris, France", 
      deadline: "2025-07-30",
      url: "https://example.com/job2",
      source: "Academic Positions EU",
      keywords_match: ["digital political economy", "blockchain", "governance"],
      relevance_score: 0.78,
      teaching: "Oui",
      language: "Anglais/Français",
      found_date: "2025-06-17"
    },
    {
      id: 3,
      title: "Postdoc in Science & Technology Studies",
      institution: "ETH Zurich - STS Lab",
      location: "Zurich, Suisse",
      deadline: "2025-09-01",
      url: "https://example.com/job3", 
      source: "Euraxess",
      keywords_match: ["sts", "technology studies", "infrastructure"],
      relevance_score: 0.72,
      teaching: "Non",
      language: "Anglais",
      found_date: "2025-06-16"
    }
  ]

  useEffect(() => {
    setJobs(mockJobs)
    setFilteredJobs(mockJobs)
    setStats({
      total_scraped: 156,
      total_relevant: 23,
      sources_processed: 8,
      last_update: new Date().toISOString()
    })
  }, [])

  useEffect(() => {
    const filtered = jobs.filter(job => 
      job.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.institution.toLowerCase().includes(searchTerm.toLowerCase()) ||
      job.keywords_match.some(keyword => 
        keyword.toLowerCase().includes(searchTerm.toLowerCase())
      )
    )
    setFilteredJobs(filtered)
  }, [searchTerm, jobs])

  const handleScraping = async () => {
    setIsLoading(true)
    // Simulation d'un appel API
    setTimeout(() => {
      setIsLoading(false)
      // Mise à jour des stats
      setStats(prev => ({
        ...prev,
        last_update: new Date().toISOString()
      }))
    }, 3000)
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    })
  }

  const getRelevanceColor = (score) => {
    if (score >= 0.8) return 'bg-green-500'
    if (score >= 0.6) return 'bg-yellow-500'
    return 'bg-orange-500'
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white/80 backdrop-blur-sm border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg flex items-center justify-center">
                <Search className="w-5 h-5 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-900">Veille Académique</h1>
                <p className="text-sm text-gray-600">STS & Cryptomonnaies</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Button variant="outline" size="sm">
                <Bell className="w-4 h-4 mr-2" />
                Alertes
              </Button>
              <Button variant="outline" size="sm">
                <Settings className="w-4 h-4 mr-2" />
                Configuration
              </Button>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Stats Dashboard */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
          >
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-gray-600">Total Scrapé</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-blue-600">{stats.total_scraped}</div>
                <p className="text-xs text-gray-500">offres trouvées</p>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-gray-600">Pertinentes</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-green-600">{stats.total_relevant}</div>
                <p className="text-xs text-gray-500">correspondances</p>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
          >
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-gray-600">Sources</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-2xl font-bold text-purple-600">{stats.sources_processed}</div>
                <p className="text-xs text-gray-500">plateformes</p>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
          >
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm font-medium text-gray-600">Dernière MAJ</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-sm font-medium text-gray-900">
                  {stats.last_update ? formatDate(stats.last_update) : 'Jamais'}
                </div>
                <p className="text-xs text-gray-500">mise à jour</p>
              </CardContent>
            </Card>
          </motion.div>
        </div>

        {/* Controls */}
        <div className="flex flex-col sm:flex-row gap-4 mb-8">
          <div className="flex-1">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-4 h-4" />
              <Input
                placeholder="Rechercher par titre, institution ou mots-clés..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="pl-10"
              />
            </div>
          </div>
          <Button 
            onClick={handleScraping}
            disabled={isLoading}
            className="bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700"
          >
            {isLoading ? (
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                className="w-4 h-4 border-2 border-white border-t-transparent rounded-full mr-2"
              />
            ) : (
              <Search className="w-4 h-4 mr-2" />
            )}
            {isLoading ? 'Scraping...' : 'Lancer Scraping'}
          </Button>
          <Button variant="outline">
            <Download className="w-4 h-4 mr-2" />
            Exporter
          </Button>
        </div>

        {/* Tabs */}
        <Tabs defaultValue="jobs" className="space-y-6">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="jobs">Offres ({filteredJobs.length})</TabsTrigger>
            <TabsTrigger value="sources">Sources</TabsTrigger>
            <TabsTrigger value="config">Configuration</TabsTrigger>
          </TabsList>

          <TabsContent value="jobs" className="space-y-4">
            <AnimatePresence>
              {filteredJobs.map((job, index) => (
                <motion.div
                  key={job.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <Card className="hover:shadow-lg transition-shadow duration-200">
                    <CardHeader>
                      <div className="flex justify-between items-start">
                        <div className="flex-1">
                          <CardTitle className="text-lg mb-2 text-gray-900">
                            {job.title}
                          </CardTitle>
                          <CardDescription className="flex items-center space-x-4 text-sm">
                            <span className="flex items-center">
                              <Building className="w-4 h-4 mr-1" />
                              {job.institution}
                            </span>
                            <span className="flex items-center">
                              <MapPin className="w-4 h-4 mr-1" />
                              {job.location}
                            </span>
                            <span className="flex items-center">
                              <Calendar className="w-4 h-4 mr-1" />
                              {formatDate(job.deadline)}
                            </span>
                          </CardDescription>
                        </div>
                        <div className="flex items-center space-x-2">
                          <div className="flex items-center space-x-1">
                            <Star className="w-4 h-4 text-yellow-500" />
                            <span className="text-sm font-medium">{job.relevance_score.toFixed(2)}</span>
                          </div>
                          <div className={`w-3 h-3 rounded-full ${getRelevanceColor(job.relevance_score)}`} />
                        </div>
                      </div>
                    </CardHeader>
                    <CardContent>
                      <div className="space-y-4">
                        <div className="flex flex-wrap gap-2">
                          {job.keywords_match.map((keyword, idx) => (
                            <Badge key={idx} variant="secondary" className="text-xs">
                              {keyword}
                            </Badge>
                          ))}
                        </div>
                        
                        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                          <div>
                            <span className="font-medium text-gray-600">Source:</span>
                            <p className="text-gray-900">{job.source}</p>
                          </div>
                          <div>
                            <span className="font-medium text-gray-600">Enseignement:</span>
                            <p className="text-gray-900">{job.teaching}</p>
                          </div>
                          <div>
                            <span className="font-medium text-gray-600">Langue:</span>
                            <p className="text-gray-900">{job.language}</p>
                          </div>
                          <div>
                            <span className="font-medium text-gray-600">Trouvé le:</span>
                            <p className="text-gray-900">{formatDate(job.found_date)}</p>
                          </div>
                        </div>

                        <div className="flex justify-end">
                          <Button variant="outline" size="sm" asChild>
                            <a href={job.url} target="_blank" rel="noopener noreferrer">
                              <ExternalLink className="w-4 h-4 mr-2" />
                              Voir l'offre
                            </a>
                          </Button>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </motion.div>
              ))}
            </AnimatePresence>

            {filteredJobs.length === 0 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-center py-12"
              >
                <Search className="w-12 h-12 text-gray-400 mx-auto mb-4" />
                <h3 className="text-lg font-medium text-gray-900 mb-2">Aucune offre trouvée</h3>
                <p className="text-gray-600">
                  {searchTerm ? 'Essayez de modifier vos critères de recherche.' : 'Lancez un scraping pour découvrir de nouvelles offres.'}
                </p>
              </motion.div>
            )}
          </TabsContent>

          <TabsContent value="sources">
            <Card>
              <CardHeader>
                <CardTitle>Sources de Données</CardTitle>
                <CardDescription>
                  Plateformes surveillées pour la veille académique
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {[
                    'Galaxie/Antares', 'Academic Positions EU', 'Euraxess', 'Jobs.ac.uk',
                    'H-Net', 'Chronicle Higher Ed', 'THEunijobs', 'HigherEdJobs'
                  ].map((source, idx) => (
                    <div key={idx} className="flex items-center justify-between p-3 border rounded-lg">
                      <span className="font-medium">{source}</span>
                      <Badge variant="outline" className="text-green-600 border-green-600">
                        Actif
                      </Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="config">
            <Card>
              <CardHeader>
                <CardTitle>Configuration</CardTitle>
                <CardDescription>
                  Paramètres de la veille et des alertes
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-6">
                  <div>
                    <h4 className="font-medium mb-2">Mots-clés surveillés</h4>
                    <div className="flex flex-wrap gap-2">
                      {['crypto', 'blockchain', 'gouvernance', 'STS', 'économie politique'].map((keyword, idx) => (
                        <Badge key={idx} variant="secondary">
                          {keyword}
                        </Badge>
                      ))}
                    </div>
                  </div>
                  
                  <div>
                    <h4 className="font-medium mb-2">Fréquence de scraping</h4>
                    <p className="text-sm text-gray-600">Quotidien à 9h00</p>
                  </div>

                  <div>
                    <h4 className="font-medium mb-2">Alertes email</h4>
                    <p className="text-sm text-gray-600">Activées pour les offres avec score > 0.7</p>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </main>
    </div>
  )
}

export default App

