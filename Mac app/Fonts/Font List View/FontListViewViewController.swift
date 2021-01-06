//
//  ViewController.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/4/21.
//

import UIKit

class FontListTableViewController: UIViewController {
    
    enum reuseIdentifiers: String {
        case fontTableViewCell = "FontTableViewCell"
    }
    
    let tableView = UITableView()
    let utilityChildViewController = UIView()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        tableView.delegate = self
        
        layoutUI()
        addChildViewControllers()
    }
    
    // Adds child view controller
    func addChildViewControllers() {
        self.add(childVC: UtilityViewController(), to: self.utilityChildViewController)
    }
    
    func add(childVC: UIViewController, to containerView: UIView) {
        addChild(childVC)
        containerView.addSubview(childVC.view)
        childVC.view.frame = containerView.bounds
        childVC.didMove(toParent: self)
    }
    
    // UI Layout
    func layoutUI() {
        view.addSubview(tableView)
        view.addSubview(utilityChildViewController)
        
        tableView.translatesAutoresizingMaskIntoConstraints = false
        utilityChildViewController.translatesAutoresizingMaskIntoConstraints = false
        
        NSLayoutConstraint.activate([
            utilityChildViewController.topAnchor.constraint(equalTo: view.topAnchor),
            utilityChildViewController.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            utilityChildViewController.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            utilityChildViewController.heightAnchor.constraint(equalToConstant: 200),
            
            tableView.topAnchor.constraint(equalTo: utilityChildViewController.bottomAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.leadingAnchor)
        ])
        
        tableView.register(FontTableViewCell.self, forCellReuseIdentifier: FontTableViewCell.reuseId)
    }
}

extension FontListTableViewController: UITableViewDelegate, UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return 3
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 5
    }
    
    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return "Font family name goes here"
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = FontTableViewCell()
        return cell
    }
}
