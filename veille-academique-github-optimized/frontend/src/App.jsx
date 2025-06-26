/*
 * Système de Veille Académique
 * Copyright (C) 2025 Développeur Principal
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <https://www.gnu.org/licenses/>.
 */

import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [jobs, setJobs] = useState([])
  const [loading, setLoading] = useState(false)
  const [activeTab, setActiveTab] = useState('dashboard')
  const [searchTerm, setSearchTerm] = useState('')
  const [stats, setStats] = useState({
    totalJobs: 0,
    highRelevance: 0,
    recentJobs: 0,
    sources: 54
  })

  // Simulation de données pour la démo
  useEffect(() => {
    const mockJobs = [
      {
        id: 1,
        title: "Postdoc in Blockchain Research",
        institution: "KU Leuven",
        location: "Belgium",
        type: "Postdoc",
        deadline: "2025-08-18",
        relevanceScore: 0.95,
        keywords: ["blockchain", "governance", "distributed systems"],
        url: "https://academicpositions.com/ad/ku-leuven/2025/post-doc-researcher-position-in-trustworthy-distributed-software-systems/235303",
        publishedDate: "2025-06-18"
      },
      {
        id: 2,
        title: "Assistant Professor - Digital Political Economy",
        institution: "Sciences Po Médialab",
        location: "France",
        type: "Assistant Professor",
        deadline: "2025-09-15",
        relevanceScore: 0.88,
        keywords: ["digital economy", "governance", "STS"],
        url: "https://example.com/sciencespo-job",
        publishedDate: "2025-06-15"
      },
      {
        id: 3,
        title: "PhD Position - Cryptocurrency Infrastructure",
        institution: "ETH Zurich",
        location: "Switzerland",
        type: "PhD",
        deadline: "2025-07-30",
        relevanceScore: 0.82,
        keywords: ["cryptocurrency", "infrastructure", "STS"],
        url: "https://example.com/eth-job",
        publishedDate: "2025-06-10"
      }
    ]
    
    setJobs(mockJobs)
    setStats({
      totalJobs: mockJobs.length,
      highRelevance: mockJobs.filter(job => job.relevanceScore >= 0.8).length,
      recentJobs: mockJobs.filter(job => new Date(job.publishedDate) > new Date('2025-06-15')).length,
      sources: 54
    })
  }, [])

  const handleScraping = async () => {
    setLoading(true)
    // Simulation d'un appel API
    setTimeout(() => {
      setLoading(false)
      alert('Scraping terminé ! Nouvelles offres ajoutées.')
    }, 3000)
  }

  const filteredJobs = jobs.filter(job =>
    job.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.institution.toLowerCase().includes(searchTerm.toLowerCase()) ||
    job.keywords.some(keyword => keyword.toLowerCase().includes(searchTerm.toLowerCase()))
  )

  const getRelevanceColor = (score) => {
    if (score >= 0.9) return '#10b981' // vert
    if (score >= 0.8) return '#f59e0b' // orange
    return '#6b7280' // gris
  }

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('fr-FR')
  }

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>🎯 Système de Veille Académique</h1>
          <p>Automatisation intelligente pour postes en STS, blockchain et gouvernance algorithmique</p>
        </div>
      </header>

      <nav className="app-nav">
        <button 
          className={activeTab === 'dashboard' ? 'nav-button active' : 'nav-button'}
          onClick={() => setActiveTab('dashboard')}
        >
          📊 Dashboard
        </button>
        <button 
          className={activeTab === 'jobs' ? 'nav-button active' : 'nav-button'}
          onClick={() => setActiveTab('jobs')}
        >
          💼 Offres ({stats.totalJobs})
        </button>
        <button 
          className={activeTab === 'sources' ? 'nav-button active' : 'nav-button'}
          onClick={() => setActiveTab('sources')}
        >
          🔍 Sources ({stats.sources})
        </button>
        <button 
          className={activeTab === 'config' ? 'nav-button active' : 'nav-button'}
          onClick={() => setActiveTab('config')}
        >
          ⚙️ Configuration
        </button>
      </nav>

      <main className="app-main">
        {activeTab === 'dashboard' && (
          <div className="dashboard">
            <div className="stats-grid">
              <div className="stat-card">
                <h3>📈 Total Offres</h3>
                <div className="stat-number">{stats.totalJobs}</div>
                <p>Offres trouvées</p>
              </div>
              <div className="stat-card">
                <h3>⭐ Haute Pertinence</h3>
                <div className="stat-number">{stats.highRelevance}</div>
                <p>Score ≥ 0.8</p>
              </div>
              <div className="stat-card">
                <h3>🆕 Récentes</h3>
                <div className="stat-number">{stats.recentJobs}</div>
                <p>Cette semaine</p>
              </div>
              <div className="stat-card">
                <h3>🌐 Sources</h3>
                <div className="stat-number">{stats.sources}</div>
                <p>Plateformes surveillées</p>
              </div>
            </div>

            <div className="action-section">
              <button 
                className={loading ? "scraping-button loading" : "scraping-button"}
                onClick={handleScraping}
                disabled={loading}
              >
                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Scraping en cours...
                  </>
                ) : (
                  <>
                    🚀 Lancer Scraping
                  </>
                )}
              </button>
              <p className="action-description">
                Lance la recherche automatisée sur les 54 sources académiques configurées
              </p>
            </div>

            <div className="recent-jobs">
              <h2>🔥 Offres Récentes</h2>
              <div className="jobs-preview">
                {jobs.slice(0, 3).map(job => (
                  <div key={job.id} className="job-preview-card">
                    <div className="job-header">
                      <h3>{job.title}</h3>
                      <span 
                        className="relevance-badge"
                        style={{ backgroundColor: getRelevanceColor(job.relevanceScore) }}
                      >
                        {(job.relevanceScore * 100).toFixed(0)}%
                      </span>
                    </div>
                    <p className="job-institution">{job.institution} • {job.location}</p>
                    <p className="job-deadline">📅 Deadline: {formatDate(job.deadline)}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'jobs' && (
          <div className="jobs-section">
            <div className="search-section">
              <input
                type="text"
                placeholder="🔍 Rechercher par titre, institution ou mots-clés..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="search-input"
              />
            </div>

            <div className="jobs-list">
              {filteredJobs.map(job => (
                <div key={job.id} className="job-card">
                  <div className="job-card-header">
                    <h3>{job.title}</h3>
                    <span 
                      className="relevance-score"
                      style={{ color: getRelevanceColor(job.relevanceScore) }}
                    >
                      Score: {job.relevanceScore.toFixed(2)}
                    </span>
                  </div>
                  
                  <div className="job-details">
                    <p><strong>🏛️ Institution:</strong> {job.institution}</p>
                    <p><strong>📍 Localisation:</strong> {job.location}</p>
                    <p><strong>💼 Type:</strong> {job.type}</p>
                    <p><strong>📅 Deadline:</strong> {formatDate(job.deadline)}</p>
                    <p><strong>📝 Publié:</strong> {formatDate(job.publishedDate)}</p>
                  </div>

                  <div className="job-keywords">
                    <strong>🏷️ Mots-clés:</strong>
                    <div className="keywords-list">
                      {job.keywords.map((keyword, index) => (
                        <span key={index} className="keyword-tag">{keyword}</span>
                      ))}
                    </div>
                  </div>

                  <div className="job-actions">
                    <a 
                      href={job.url} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      className="job-link"
                    >
                      🔗 Voir l'offre
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'sources' && (
          <div className="sources-section">
            <h2>🌐 Sources Surveillées</h2>
            <div className="sources-grid">
              <div className="source-category">
                <h3>🇪🇺 Plateformes Européennes</h3>
                <ul>
                  <li>Academic Positions EU</li>
                  <li>Euraxess</li>
                  <li>Jobs.ac.uk</li>
                  <li>H-Net Job Guide</li>
                </ul>
              </div>
              <div className="source-category">
                <h3>🇫🇷 Institutions Françaises</h3>
                <ul>
                  <li>Galaxie/Odyssée</li>
                  <li>APEC</li>
                  <li>CNRS, EHESS, IFRIS</li>
                  <li>Mines, Télécom, INSA</li>
                </ul>
              </div>
              <div className="source-category">
                <h3>🏫 Écoles de Commerce</h3>
                <ul>
                  <li>FNEGE</li>
                  <li>HEC, ESSEC, EDHEC</li>
                  <li>EM Lyon, Audencia</li>
                  <li>SKEMA</li>
                </ul>
              </div>
              <div className="source-category">
                <h3>🌍 International</h3>
                <ul>
                  <li>Chronicle of Higher Education</li>
                  <li>Nature Careers</li>
                  <li>Science Careers</li>
                  <li>ResearchGate Jobs</li>
                </ul>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'config' && (
          <div className="config-section">
            <h2>⚙️ Configuration</h2>
            
            <div className="config-group">
              <h3>🏷️ Mots-clés de Recherche</h3>
              <div className="keywords-config">
                <div className="keyword-category">
                  <h4>Blockchain & Crypto</h4>
                  <div className="keyword-tags">
                    <span className="config-tag">blockchain</span>
                    <span className="config-tag">cryptocurrency</span>
                    <span className="config-tag">bitcoin</span>
                    <span className="config-tag">ethereum</span>
                    <span className="config-tag">web3</span>
                  </div>
                </div>
                <div className="keyword-category">
                  <h4>Gouvernance</h4>
                  <div className="keyword-tags">
                    <span className="config-tag">governance</span>
                    <span className="config-tag">algorithmic governance</span>
                    <span className="config-tag">digital governance</span>
                    <span className="config-tag">decentralized</span>
                  </div>
                </div>
                <div className="keyword-category">
                  <h4>STS & Recherche</h4>
                  <div className="keyword-tags">
                    <span className="config-tag">STS</span>
                    <span className="config-tag">digital political economy</span>
                    <span className="config-tag">critical data studies</span>
                    <span className="config-tag">infrastructure</span>
                  </div>
                </div>
              </div>
            </div>

            <div className="config-group">
              <h3>🔧 Paramètres de Scraping</h3>
              <div className="config-options">
                <label>
                  <input type="checkbox" defaultChecked />
                  Scraping automatique quotidien
                </label>
                <label>
                  <input type="checkbox" defaultChecked />
                  Alertes email pour nouvelles offres
                </label>
                <label>
                  <input type="checkbox" defaultChecked />
                  Sauvegarde Google Drive
                </label>
                <label>
                  <input type="checkbox" />
                  Mode debug (logs détaillés)
                </label>
              </div>
            </div>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>
          🎯 Système de Veille Académique • 
          <a href="https://www.gnu.org/licenses/gpl-3.0" target="_blank" rel="noopener noreferrer">
            GPL v3
          </a> • 
          54 sources surveillées • 
          42 mots-clés spécialisés
        </p>
      </footer>
    </div>
  )
}

export default App

