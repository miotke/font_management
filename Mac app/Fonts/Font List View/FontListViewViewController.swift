//
//  ViewController.swift
//  Fonts
//
//  Created by Miotke, Andrew on 1/4/21.
//

import UIKit

class FontListTableViewController: UITableViewController {
    
    enum reuseIdentifiers: String {
        case fontTableViewCell = "FontTableViewCell"
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(FontTableViewCell.self, forCellReuseIdentifier: FontTableViewCell.reuseId)
    }
}

extension FontListTableViewController {
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 3
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 5
    }
    
    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        return "Font family name goes here"
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = FontTableViewCell()
        return cell
    }
}
