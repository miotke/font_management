//
//  UtilityViewController.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/5/21.
//

import UIKit

class UtilityViewController: UIViewController {
    
    /*
     Utility view controller will sit on top of the
     table view showing the login status bar, search bar,
     and any other utilities that are needed for this app.
     
     */
    
    // UI Elements
    let authenticationStatusIcon = UILabel()
    let authenticationButton = SystemButton() // Only used if authentication is set to false
    let searchBar = UISearchBar()
    
    var isAuthenticated = true
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.backgroundColor = UIColor.systemGray5
        layoutUI()
        tempValues()
        authenticationButton.addTarget(self, action: #selector(authenticationButtonAction), for: .touchUpInside)
    }
    
    private func tempValues() {
        if isAuthenticated == true {
            authenticationStatusIcon.text = "🟢"
            authenticationButton.setTitle("Sign out", for: .normal)
        } else {
            authenticationStatusIcon.text = "🔴"
            authenticationButton.setTitle("Sign in", for: .normal)
        }
    }
    
    @objc func authenticationButtonAction(sender: UIButton) {
        if isAuthenticated == true {
            isAuthenticated = false
            authenticationStatusIcon.text = "🔴"
            authenticationButton.setTitle("Sign in", for: .normal)
        } else {
            isAuthenticated = true
            authenticationStatusIcon.text = "🟢"
            authenticationButton.setTitle("Sign out", for: .normal)
        }
    }
    
    private func layoutUI() {
        
        let authenticationStackView = UIStackView(arrangedSubviews: [authenticationStatusIcon, authenticationButton])
        authenticationStackView.axis = .vertical
        authenticationStackView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(authenticationStackView)
        
        view.addSubview(searchBar)
        searchBar.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            authenticationStackView.topAnchor.constraint(equalTo: view.topAnchor, constant: 25),
            authenticationStackView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -10),
            authenticationStackView.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -25),
            authenticationStackView.leadingAnchor.constraint(equalTo: searchBar.trailingAnchor, constant: 10),
            
            searchBar.topAnchor.constraint(equalTo: view.topAnchor, constant: 25),
            searchBar.trailingAnchor.constraint(equalTo: authenticationStackView.leadingAnchor, constant: -30),
            searchBar.bottomAnchor.constraint(equalTo: view.bottomAnchor, constant: -25),
            searchBar.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 10),
        ])
        
    }
}
